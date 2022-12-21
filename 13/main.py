import re

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def read_packets(lines):
    packet_pairs = []
    packet1 = ''
    packet2 = ''
    one_read  = False
    for line in lines:
        if line == '':
            
            one_read = False
            continue
        if one_read:
            packet2 = line
            packet_pairs.append((packet1, packet2))
        else:
            packet1 = line
            one_read = True
    return packet_pairs
   
def compare(left, right):
    
    if len(left) == 0 and len(right) != 0:
        print('Left side ran out of items, so inputs are in the right order')
        return True
    for i in range(0, len(left)):

        if i >= len(right):
            print('Right side ran out of items, so inputs are not in the right order')
            return False

        l = left[i]
        r = right[i]
            
        print('Comparing {} v {}'.format(l, r))

        if type(l) is int and type(r) is int:
            if l < r:
                print('Left side is smaller, so inputs are in the right order')
                return True
            if l > r:
                print('Right side is smaller, so inputs are not in the right order')
                return False       
        elif type(l) is int:
            print('Mixed types; convert left to [{}] and retry comparison'.format(l))
            l = [l]
            result = compare(l, r)
            if result is not None:
                return result
        elif type(r) is int:
            print('Mixed types; convert right to [{}] and retry comparison'.format(r))
            r = [r]
            result = compare(l, r)
            if result is not None:
                return result
        else:
            result = compare(l, r)
            if result is not None:
                return result
    
    if len(left) < len(right):
        print('Left side ran out of items, so inputs are in the right order')
        return True
    
    return None
            
         
def part1():
    pairs = read_packets(get_input())
    sum = 0
    for i, pair in enumerate(pairs):
        left = eval(pair[0])
        right = eval(pair[1])
        print('== Pair {} =='.format(i+1))
        if compare(left, right):
            sum += (i + 1)
        print()
    print(sum)

def main():
    part1()
    packets = [[[2]], [[6]]]
    lines = get_input()
    for line in lines:
        if line == '':
            continue
        packets.append(eval(line))
        
    l = len(packets)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            print(j)
            if not compare(packets[j], packets[j+1]):
                packets[j], packets[j+1] = packets[j+1], packets[j]
    
    divider_index_1 = packets.index([[2]]) + 1
    divider_index_2 = packets.index([[6]]) + 1
    print('[[2]] at index {}'.format(divider_index_1))
    print('[[6]] at index {}'.format(divider_index_2))
    print(divider_index_1 * divider_index_2)
    
if __name__ == '__main__':
    main()