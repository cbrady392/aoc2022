import re

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def add_sizes(path, size):
    while path != '/' and path != '':
        print('adding size {} to dir {}'.format(size, path))
        try:
            dir_sizes[path] += size 
        except KeyError:
            dir_sizes[path] = size
        up_one_pos = path.rfind('/')
        path = path[:up_one_pos]
        
    print('adding size {} to dir /'.format(size))
    dir_sizes['/'] += size 
dir_sizes = {'/': 0}

def main():
    instructions = get_input()
    pwd = '/'
    for instruction in instructions:
        #print('pwd {}'.format(pwd))
        if instruction[2:4] == 'cd':
            if instruction[5:7] == '..':
                print('going up one dir')
                up_one_pos = pwd.rfind('/')
                pwd = pwd[:up_one_pos]
            else:
                new_dir = instruction[5:]
                print('changing directory to {}'.format(new_dir))
                if pwd != '/':
                    pwd += '/'
                pwd += '{}'.format(new_dir)

        elif instruction[2:4] == 'ls':
            pass
        elif instruction[:3] == 'dir':
            pass
        else:
            m = re.match(r'^\d+', instruction)
            
            if m is not None:
                add_sizes(pwd, int(m[0]))
    
    sum = 0
    
    for k, ds in dir_sizes.items():
        if ds < 100000:
            print(k)
            sum += ds 
    print(sum)
    
    total_space = 70000000
    required_space = 30000000
    
    free_space = total_space - dir_sizes['/']
    min_to_delete = required_space - free_space
    
    sorted_dir_sizes = sorted(dir_sizes.items(), key=lambda x: x[1])
    for dir in sorted_dir_sizes:
        if dir[1] > min_to_delete:
            print(dir)
            break
    
    
    
if __name__ == '__main__':
	main()