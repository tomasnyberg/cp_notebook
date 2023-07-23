import sys
import math
from collections import defaultdict
lines = list(map(str.strip, sys.stdin.readlines()))
from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

def count_pairs_from_dict(d):
    return sum(val * (val - 1) // 2 for val in d.values())

def solve_morning_star(points):
    x_coords = defaultdict(int)
    y_coords = defaultdict(int)
    slope1 = defaultdict(int)
    slope_minus1 = defaultdict(int)
    
    for x, y in points:
        x_coords[Wrapper(x)] += 1
        y_coords[Wrapper(y)] += 1
        slope1[Wrapper(x - y)] += 1
        slope_minus1[Wrapper(x + y)] += 1
    result = 0
    for d in [x_coords, y_coords, slope1, slope_minus1]:
        result += count_pairs_from_dict(d)
    
    return result
ii = 1
t = int(lines[0])
for _ in range(t):
    n = int(lines[ii])
    ii += 1
    points = [tuple(map(int, lines[ii + i].split())) for i in range(n)]
    ii += n
    print(solve_morning_star(points) * 2)
