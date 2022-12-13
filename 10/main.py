import math
def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines
    

def main():
    instrs = get_input()
    x = 1
    executing = 0
    index = 0
    line = ''
    for cycle in range(1, 241):
        # Start Cycle
        if executing == 0:

            instr = instrs[index]
            index += 1
            if instr[:4] == 'addx':
                val = int(instr[5:])
                
                executing = 2
            if instr[:4] == 'noop':
                val = 0
                executing = 1
            print('Start Cycle\t{}: begin executing {}'.format(cycle, instr))
                
        # During Cycle
        draw_pixel = len(line) % 40
        print('During cycle\t{}: CRT draws pixel in position {}'.format(cycle, draw_pixel))

        if draw_pixel >= x - 1 and draw_pixel <= x + 1:
            line += '#'
        else:
            line += ' '
            
        
        # End Cycle 
        executing -= 1
        if executing == 0:
            x += val
            print('End of cycle\t{}: finish executing {} (Register X is now {}'.format(cycle, instrs[index-1], x))

        
        print()
    for i in range(0 ,240, 40):
        print(line[i:i+40])

            
        
        
        
        
        

    
    
    
        
    
if __name__ == '__main__':
    main()