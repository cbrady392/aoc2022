settled_sand = []

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines
	
   
def map_rocks(line):
    coordinates = line.split('->')
    current = None
    rocks = []
    for c in coordinates:
        if current is None:
            current = c.strip().split(',')
            cx = int(current[0])
            cy = int(current[1])
            rocks.append((cx, cy))
        else:
            new_position = c.strip().split(',')
            nx = int(new_position[0])
            ny = int(new_position[1])
            x_diff = nx - cx

            x_dir = 0
            y_dir = 0
            if x_diff > 0:
                x_dir = 1
            if x_diff < 0:
                x_dir = -1
            y_diff = ny - cy
            if y_diff > 0:
                y_dir = 1
            if y_diff < 0:
                y_dir = -1           

            if x_dir != 0:
                for i in range(0, x_diff + x_dir, x_dir):
                    if (cx + i, cy) not in rocks:
                        rocks.append((cx + i, cy))

            if y_dir != 0:
                for i in range(0, y_diff + y_dir, y_dir):
                    if (cx, cy + i) not in rocks:
                        rocks.append((cx, cy + i))               
            cx = nx
            cy = ny
                
    return rocks

def find_floor(lines):
    max_y = 0
    for line in lines:
        line_coords = line.split('->')
        for lc in line_coords:
            c = lc.strip().split(',')
            if int(c[1]) > max_y:
                max_y = int(c[1])
                    
    floor = [(x, max_y + 2) for x in range(0, 1000)]
    return floor
    
def draw(lx, rx, uy, dy, rocks):
    output = []
    for i in range(uy, dy):
        line = ''
        for j in range(lx, rx):
            if j == 500 and i == 0:
                c = '+'
            elif (j, i) in rocks:
                c = '#'
            elif (j, i) in settled_sand:
                c = 'o'
            else:
                c = '.'
            line += c
        output.append(line)
    for line in output:
        print(line)
        

def drop_sand(rocks, lower_bound):
    SAND_INIT = (500 , 0)
    falling_sand = SAND_INIT

    while True:
        down = (falling_sand[0], falling_sand[1] + 1)
        down_left = (falling_sand[0] - 1 , falling_sand[1] + 1)
        down_right = (falling_sand[0] + 1 , falling_sand[1] + 1)
        if down in rocks or down in settled_sand:
            if down_left in rocks or down_left in settled_sand:
                if down_right in rocks or down_right in settled_sand:
                    settled_sand.append(falling_sand)
                    if falling_sand == SAND_INIT:
                        return False
                    return True
                else:
                    falling_sand = down_right              
            else:
                falling_sand = down_left
        else:
            falling_sand = down

        if falling_sand[1] >= lower_bound:
            return False
    
def main():	
    rocks = []
    TEST_BOUNDS = [480, 515, 0, 14]
    REAL_BOUNDS = [440, 520, 0, 185]
    b = REAL_BOUNDS
    part2 = True
    lines = get_input()
    for line in lines:
        rocks += map_rocks(line)
    if part2:
        rocks += find_floor(lines)

    drop = True
    while drop:
        drop = drop_sand(rocks, b[3])
        #draw(b[0], b[1], b[2], b[3], rocks)

    print(len(settled_sand))
        
if __name__ == '__main__':
    main()