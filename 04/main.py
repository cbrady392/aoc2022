def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines
	
def format_range(line):
    a, b = line.split(',')
    min_a, max_a = a.split('-')
    min_b, max_b = b.split('-')
    min_a = int(min_a)
    min_b = int(min_b)
    max_a = int(max_a)
    max_b = int(max_b)
    return min_a, max_a, min_b, max_b
    
def range_contains_another(min_a, max_a, min_b, max_b):
    
    if min_b >= min_a and max_b <= max_a:
        return True
    if min_a >= min_b and max_a <= max_b:
        return True
    return False

def range_overlaps_another(min_a, max_a, min_b, max_b):
    
    if min_a >= min_b and min_a <= max_b:
        return True
    if max_a >= min_b and max_a <= max_b:
        return True
    if min_b >= min_a and min_b <= max_a:
        return True
    if max_b >= min_a and max_b <= max_a:
        return True
    return False
    
def main():
    contain_count = 0
    overlap_count = 0
    for line in get_input():
        min_a, max_a, min_b, max_b = format_range(line)
        if range_contains_another(min_a, max_a, min_b, max_b):
            contain_count += 1
        if range_overlaps_another(min_a, max_a, min_b, max_b):
            overlap_count += 1
    
    print(contain_count, overlap_count)

if __name__ == '__main__':
	main()