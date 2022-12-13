from dataclasses import dataclass

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

@dataclass
class Coord:
    x: int
    y: int

@dataclass
class Vector:
    x: int
    y: int

UP = Vector(x = 0, y = -1)
DN = Vector(x = 0, y = 1)
LT = Vector(x = -1, y = 0)
RT = Vector(x = 1, y = 0)
tmap = get_input()

def is_visible(x, y):
    val = tmap[x][y]
    
    visible = check_to_edge(val, x, y, UP) or check_to_edge(val, x, y, DN) or check_to_edge(val, x, y, RT) or check_to_edge(val, x, y, LT)
    return visible
    
def check_to_edge(val, x, y, vector):
    x += vector.x
    y += vector.y
    step = 1
    while x >= 0 and x < len(tmap[0]) and y >= 0 and y < len(tmap):
        if tmap[x][y] >= val:
            return False
        x += vector.x
        y += vector.y
        step += 1
    return True

def check_tree_height(val, x, y, vector):
    x += vector.x
    y += vector.y
    step = 1
    while x > 0 and x < len(tmap[0])-1 and y > 0 and y < len(tmap)-1:
        if tmap[x][y] >= val:
            return step
        x += vector.x
        y += vector.y
        step += 1
    return step
    
def calc_score(x, y):
    val = tmap[x][y]
    print(val)
    print(check_tree_height(val, x, y, DN))
    return check_tree_height(val, x, y, LT) * check_tree_height(val, x, y, RT) * check_tree_height(val, x, y, UP) * check_tree_height(val, x, y, DN)
    
def main():
  
    sum = 0
    max_score = 1
    
    for x in range(0, len(tmap[0])):
        for y in range(0, len(tmap)):
           if is_visible(x, y):
                sum += 1
           score = calc_score(x, y)
           #score = 0
           #score = 0
           if score > max_score:
                max_score = score
    print(sum)
    print(max_score)
    #print(calc_score(3,2))
    
    
    
if __name__ == '__main__':
	main()