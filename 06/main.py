def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def string_contains_duplicate_chars(s):
    for c in s:
        if s.count(c) > 1:
            return False
    return True
    
MESSAGE_SIZE = 14
def  main():
    input = get_input()[0]
    #input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    for i in range(0, len(input) - (MESSAGE_SIZE - 1)):
        if string_contains_duplicate_chars(input[i:i+MESSAGE_SIZE]):
            print(i+MESSAGE_SIZE)
            return
        
    
    
    


if __name__ == '__main__':
	main()