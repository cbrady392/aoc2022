from dataclasses import dataclass
import re
import copy
import math
from tqdm import tqdm

def get_input():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


@dataclass
class Point:
    x: int
    y: int

U = Point(x = 0, y = -1)
D = Point(x = 0, y = 1)
L = Point(x = -1, y = 0)
R = Point(x = 1, y = 0)

RU = Point(x = 1, y = -1)
RD = Point(x = 1, y = 1)
LU = Point(x = -1, y = -1)
LD = Point(x = -1, y = 1)
ALL_DIR = [U, D, L, R]
RING_DIR = [RU, RD, LD, LU]

def parse_line(line):
    p = r'[yx]=(\-?\d+)'
    m = re.findall(p, line)
    return Point(x = int(m[0]), y = int(m[1])), Point(x = int(m[2]), y = int(m[3]))
    
def find_ring_points(sb_pairs):
    ring_points = []
    for sb in tqdm(sb_pairs):
        # print(sb[0], sb[1])
        d = calc_distance(sb[0], sb[1])
        x = sb[0].x - (d + 1)
        y = sb[0].y

        for i in tqdm(range(0, (d+1) * 4)):
            d_index = math.floor( i / (d+1) )
            # print(i, RING_DIR[d_index], Point(x = x, y = y))
            ring_points.append(Point(x = x, y = y))
            x += RING_DIR[d_index].x
            y += RING_DIR[d_index].y
            
    
    return ring_points
 

def calc_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def covered_by_sensors(point, sb_pairs):
    for sb in sb_pairs:
        if point == sb[1]:
            return False
        sensor_point_distance = calc_distance(point, sb[0])
        sensor_beacon_distance = calc_distance(sb[0], sb[1])
        if sensor_point_distance <= sensor_beacon_distance:
            return True
    return False

def part1():
    lines = get_input()
    sb_pairs = []
    for line in lines:
        sb_pairs.append(parse_line(line))
    sum = 0
    ROW = 2000000
    MIN_X = -10000000
    MAX_X = 10000000
    for i in range(MIN_X, MAX_X):
        if i % 10000 == 0:
            print(i)
        if covered_by_sensors(Point(x = i, y = ROW), sb_pairs):
            sum +=1
    print(sum)
 
def main():

    lines = get_input()
    sb_pairs = []
    possible_answers = []
    for line in lines:
        sb_pairs.append(parse_line(line))
    for rp in tqdm(find_ring_points(sb_pairs)):
        if rp.x < 0 or rp.y < 0 or rp.x > 4000000 or rp.y > 4000000:
            continue
        if not covered_by_sensors(rp, sb_pairs):
            possible_answers.append(rp)
            
    for pa in possible_answers:
        print(pa)
        print((pa.x * 4000000) + pa.y)
            
if __name__ == '__main__':
    main()