import re
def get_input():
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]
    return lines
	
def create_stacks(lines):
    stacks = {}
    for i in range(1,10):
        stacks[i] = []
    lines.reverse()
    for line in lines:
        for index, i in enumerate(range(1, 34, 4)):
            c = line[i]
            if(c != ' ' ):
                stacks[index+1].append(c)
    return stacks

def parse_instruction(line):
    m = re.findall(r'\d+', line)
    return int(m[0]), int(m[1]), int(m[2])
    
    
def main():
    all_lines = get_input()
    stacks = create_stacks(all_lines[:8])
    stacks2 = {key: value[:] for key, value in stacks.items()}
    
    instructions = all_lines[10:]
    
    # instructions = instructions[:5]
    # print(instructions)
    
    # Part 1 - Crate Mover 9000
    for instr in instructions:
        amount, source, dest = parse_instruction(instr)
        for i in range(0, amount):
            temp = stacks[source].pop()
            stacks[dest].append(temp)
            
    # print(stacks)
    
    for k,v in stacks.items():
        print(v[-1], sep='', end='')
        
    print('\n----')
    # Part 2 - Crate Mover 9001
    stacks = stacks2

    for instr in instructions:
        amount, source, dest = parse_instruction(instr)
        stacks[dest] += stacks[source][-amount:]
        del stacks[source][-amount:]
    
    for k,v in stacks.items():
        print(v[-1], sep='', end='')
    
if __name__ == '__main__':
	main()