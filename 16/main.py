from tqdm import tqdm
from collections import deque
from dataclasses import dataclass
from itertools import product
import re
import time
start_time = time.time()

valves = {}
flow = {}

@dataclass
class Branch:
    path: list[list[str]]
    minutes: list[int]
    opened: dict[str, int]
    
def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def parse_valves():
    for line in get_input():
        key = line[6:8]
        leads_to = re.search(r'valves? ([A-Z, ]+)', line).group(1)
        valves[key] = [lead.strip() for lead in leads_to.split(',')]
        
        flow[key] = int(re.search(r'=(\d+)', line).group(1))
     
def find_path(start, end):
    queue = deque([[start]])
    valves_visited = set()
    
    while queue:
        path = queue.popleft()
        current_valve = path[-1]
        
        if current_valve not in valves_visited:
            next_possible_valves = valves[current_valve]
            
            for pv in next_possible_valves:
                new_path = list(path)
                new_path.append(pv)
                #print(new_path)
                queue.append(new_path)
                #print(queue)
                if pv == end:
                    return len(new_path) - 1
            
            valves_visited.add(current_valve)
    return None
             
            
def open_valves(current_valve, time_remaining, prev_valve='', path=[]):
    pass
            
def main():
    parse_valves()

    valves_to_open = [v for v in valves.keys() if flow[v] > 0]

    #time = 30
    max_time = 26
    start = 'AA'
    max_pressure = 0
    #branch_stack = [Branch(path = [start], minutes = 0, opened = {})]
    branch_stack = [Branch(path = [[start], [start]], minutes = [0, 0], opened = {})]
    
    while branch_stack:
     
        current_branch = branch_stack.pop()
        print(current_branch)

        
        if (current_branch.minutes[0] >= max_time and current_branch.minutes[1] >= max_time) or len(current_branch.opened.keys()) == len(valves_to_open):
            pressure = 0
            
            for k, v in current_branch.opened.items():
                opened_minutes = max(max_time - v, 0)
                pressure += flow[k] * opened_minutes
           
            max_pressure = max(max_pressure, pressure)
            
        else:
        
            current_valves = [current_branch.path[0][-1], current_branch.path[1][-1]]
            
            valves_to_open_combos = [c for c in product(valves_to_open, repeat=2) if len(set(c)) == 2]
            valves_to_open_combos = [l for l in valves_to_open_combos if l[0] not in current_branch.opened.keys() and l[1] not in current_branch.opened.keys()]
                    
            for next_valve_combo in valves_to_open_combos:
                
                new_open_valves = current_branch.opened.copy()
                if next_valve_combo[0] not in current_branch.opened.keys() and next_valve_combo[1] not in current_branch.opened.keys():
                    new_time = []
                    new_path = []
                    #print(next_valve_combo)
                    for i in range(0, len(current_valves)):
                        new_time.append(current_branch.minutes[i])
                        new_path.append(list(current_branch.path[i]))
                        if current_branch.minutes[i] <= max_time:
                            
                            time_to_valve = find_path(current_valves[i], next_valve_combo[i])
                            open_time = 1
                            if time_to_valve + open_time <= max_time:
       
                                new_time[i] += time_to_valve + open_time
                            
                                new_open_valves[next_valve_combo[i]] = new_time[i]
                            
                                new_path[i].append(next_valve_combo[i])
                    
                    new_branch = Branch(path = new_path, minutes = new_time, opened = new_open_valves)
                  
                branch_stack.append(new_branch)
                    
                    
    print(max_pressure)
    print("%s seconds" % (time.time() - start_time))
    #open_valves('AA', TIME)
    #print(valves)
    #print(all_paths)
	
if __name__ == '__main__':
    main()