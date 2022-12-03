
def convert(c):
    o = ord(c)
    if o > 96:
        o -= 96
    else:
        o -= 38
    return o

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines
    
def split_line(line):
    l = int(len(line) / 2)
    return line[:l], line[l:]
 
def character_is_in_all_lines(c, lines):
    for line in lines:
        if c not in line:
            return False
    return True
    
def find_common_character_value(lines):
    for c in lines[0]:
        if character_is_in_all_lines(c, [lines[1], lines[2]]):
            return convert(c)

def main():
    # Part 1
    sum = 0
    lines = get_input()
    for index, line in enumerate(lines):
        found_items = []
        #if index > 2:
        #    break
        left, right = split_line(line)
        #print(index, "|{}|{}|".format(left,right))
        for c in left:
            if c in right:
                if c not in found_items:
                    sum += convert(c)
                    found_items.append(c)
    print(sum)
    
    # Part 2
    sum = 0
    for i in range(0, len(lines), 3):
        lines_3 = [lines[i], lines[i+1], lines[i+2]]
        sum += find_common_character_value(lines_3)
              
    print(sum)
                
   

if __name__ == '__main__':
	main()