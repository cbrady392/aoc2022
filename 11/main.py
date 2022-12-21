import operator
import math

monkeys = []
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv }

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def apply_operation(op, val):
    operand1, opr, operand2 = op.split(' ')
    if operand2 == 'old':
        b = val
    else:
        b = int(operand2)
    return ops[opr](val, b)
    
def parse_monkey(instructions):
    current_monkey = 0
    for instruction in instructions:
        if instruction[:4] == 'Monk':
            monkeys.append({'times_inspected': 0})
            current_monkey = int(instruction.split(' ')[1][:-1])
        if instruction[:4] == 'Star':
            monkeys[current_monkey]['items'] = [int(x.strip()) for x in instruction.split(':')[1].split(',')]
        if instruction[:4] == 'Oper':
            monkeys[current_monkey]['op'] = instruction.split('=')[1].strip()
        if instruction[:4] == 'Test':
            monkeys[current_monkey]['test'] = int(instruction.split(' ')[-1])
        if instruction[:4] == 'If t':
            monkeys[current_monkey]['true'] = int(instruction.split(' ')[-1])
        if instruction[:4] == 'If f':
            monkeys[current_monkey]['false'] = int(instruction.split(' ')[-1])

def inspect(item, monkey, mod):
    item = apply_operation(monkey['op'], item)
    item = item % mod
    if item % monkey['test'] == 0:
        monkeys[monkey['true']]['items'].append(item)
    else:
        monkeys[monkey['false']]['items'].append(item)

    monkey['times_inspected'] += 1
            
def main():
    parse_monkey(get_input())
    # print(monkeys)
    rounds = 10000
    mod = 1
    for m in monkeys:
        mod *= m['test']
        
    for i in range(0, rounds):
        # if i % 1000 == 0:
        #     for j, m in enumerate(monkeys):
        #         print(i, m['times_inspected'])
        #     print('----')
        for monkey in monkeys:
            while len(monkey['items']) > 0:
                inspect(monkey['items'].pop(0), monkey, mod)

    for i, m in enumerate(monkeys):
        print(i, m['times_inspected'])
                
                
    
    
    
if __name__ == '__main__':
    main()