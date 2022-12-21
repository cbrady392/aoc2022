from dataclasses import dataclass
import copy
def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

TOPMAP = get_input()

@dataclass
class Vector:
    x: int
    y: int

UP = Vector(x = 0, y = -1)
DN = Vector(x = 0, y = 1)
LT = Vector(x = -1, y = 0)
RT = Vector(x = 1, y = 0)
ALL_DIR = [UP, DN, LT, RT]

def starting_position():
    for y, line in enumerate(TOPMAP):
        for x, c in enumerate(line):
            if c == 'S':
                return x, y

def ending_position():
    for y, line in enumerate(TOPMAP):
        for x, c in enumerate(line):
            if c == 'E':
                return x, y
                
def can_move(x, y, d, cp):
    # If move would put cursor out of bounds, return False
    # print(y, d, len(TOPMAP))

    if x + d.x < 0 or y + d.y < 0 or x + d.x > len(TOPMAP[0]) - 1 or y + d.y > len(TOPMAP) - 1:
        return False

    if (x + d.x, y + d.y) in cp:
        return False
        
    current_elevation = TOPMAP[y][x]
    next_elevation = TOPMAP[y + d.y][x + d.x]
    # print(current_elevation, next_elevation)
    if current_elevation == 'S' and next_elevation == 'a':
        return True
    if current_elevation == 'z' and next_elevation == 'E':
        return True
        
    if ord(next_elevation) - ord(current_elevation) > 1 or next_elevation == 'E':
        return False
 
    return True

def move(x, y, cp):
    valid_dir = [d for d in ALL_DIR if can_move(x, y, d, cp)]
    if len(valid_dir) == 0:
        return

    available_spaces = []
    for vd in valid_dir:
        new_x = x + vd.x
        new_y = y + vd.y

        available_spaces.append((new_x, new_y))
    return available_spaces

def part1(x, y):
    covered_path = []
    covered_path.append((x, y))
    next_trails = [[(x, y)]]

    searching = True
    steps = 0
    while searching:


        steps += 1
        trails = copy.deepcopy(next_trails)
        # print(steps, trails)
        next_trails = []
        while trails:
            trail = trails.pop()
            split_path = False
            new_spaces = move(trail[-1][0], trail[-1][1], covered_path)
            if new_spaces is None:
                continue
            temp_trail = copy.deepcopy(trail)
            for ns in new_spaces:
                covered_path.append(ns)
                if not split_path:
                    trail.append(ns)
                    split_path = True
                    next_trails.append(trail)
                else:
                    new_trail = copy.deepcopy(temp_trail)
                    new_trail.append(ns)
                    next_trails.append(new_trail)                    
            #print(steps, i, t)

            if ending_position() in trail:
                searching = False
        if steps > 500:
            break

    return steps
    
def part2():
    min_steps = 500
    for y, line in enumerate(TOPMAP):
        for x, c in enumerate(line):
            if c == 'a':

                steps = part1(x, y)
                print('starting a at ({},{}): {} steps'.format(x, y, steps))
                if steps < min_steps:
                    min_steps = steps
    print(min_steps)
                
    
def main():
    x, y = starting_position()
    print(part1(x, y))
    part2()
    
if __name__ == '__main__':
    main()