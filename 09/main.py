from dataclasses import dataclass
# Part 2 - 6339 too high

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines
    
    
@dataclass
class Vector:
    x: int
    y: int

UP = Vector(x = 0, y = -1)
DN = Vector(x = 0, y = 1)
LT = Vector(x = -1, y = 0)
RT = Vector(x = 1, y = 0)


def vadd(H, vec):
    return Vector(x = H.x + vec.x, y = H.y + vec.y)

def vcopy(V):
    return Vector(x = V.x, y = V.y)
    
def move_tail(h, t):
    mv = Vector(x = 0, y = 0)
    # Moves Left
    if h.x - t.x < -1:
        mv = vadd(mv, LT)
        # Diagonal move
        if h.y - t.y < 0:
            mv = vadd(mv, UP)
        if h.y - t.y > 0:
            mv = vadd(mv, DN)
    # Moves Right
    if h.x - t.x > 1:
        mv = vadd(mv, RT)
        # Diagonal move
        if h.y - t.y < 0:
            mv = vadd(mv, UP)
        if h.y - t.y > 0:
            mv = vadd(mv, DN)

    # Moves Up
    if h.y - t.y < -1:
        mv = vadd(mv, UP)
        # Diagonal move
        if h.x - t.x < 0:
            mv = vadd(mv, LT)
        if h.x - t.x > 0:
            mv = vadd(mv, RT)
    # Moves Down
    if h.y - t.y > 1:
        mv = vadd(mv, DN)
        # Diagonal move
        if h.x - t.x < 0:
            mv = vadd(mv, LT)
        if h.x - t.x > 0:
            mv = vadd(mv, RT)
            
    if mv.x > 1:
        mv.x = 1
    if mv.x < -1:
        mv.x = -1
    if mv.y > 1:
        mv.y = 1
    if mv.y < -1:
        mv.y = -1
    return vadd(t, mv)
    
def main():

    MAX_TAIL_LENGTH = 9
    TAIL = [Vector(x = 0, y = 0) for i in range(0, MAX_TAIL_LENGTH+1)]

    tail_positions = []
    
    instrs = get_input()
    tail_positions = []
    for instr in instrs:
        
        dir = instr[0]
        steps = instr[2:]
        # print(dir, steps)

        for i in range(0, int(steps)):
            curr_dir = Vector(x = 0, y  = 0)
            if dir == 'U':
                curr_dir = UP
            if dir == 'D':
                curr_dir = DN
            if dir == 'L':
                curr_dir = LT
            if dir == 'R':
                curr_dir = RT
            #print(TAIL[0], curr_dir)
            TAIL[0] = vadd(TAIL[0], curr_dir)
            #print(TAIL[0], curr_dir)
            for j in range(1, len(TAIL)):
                TAIL[j] = move_tail(TAIL[j-1], TAIL[j])
              
            if TAIL[-1] not in tail_positions:
                #print(TAIL[-1])
                tail_positions.append(TAIL[-1])
         
            # for t in TAIL:
            #    print(t)
            #    pass
            # print('----')
    # Need to set a current direction, then move head + tail posistions based of off that.
            
    print(len(tail_positions))
    #print(tail_positions)
        
            
            
    
if __name__ == '__main__':
    main()