
def main():
    tracker = []
    new_entry = True

    with open('input.txt') as f:
        
        for line in f.readlines():
            if line == '\n':
                new_entry = True
                continue
            
            try:
                value = int(line.strip())
            except ValueError:
                value = 0
                
            if new_entry:
                tracker.append(value)
                new_entry = False
            else:
                tracker[-1] += value
                
    tracker.sort(reverse = True)
    print(tracker[0])
    print(tracker[:3])
    sum = 0
    for t in tracker[:3]:
        sum += t
    print(sum)

if __name__ == '__main__':
    main()
		