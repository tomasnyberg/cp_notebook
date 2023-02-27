import sys
import bisect
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))

def calculate_cost(programs, start, end, hot, cold):
    hotstate = -1
    time = 0
    for i in range(start, end):
        if programs[i] == hotstate:
            time += hot[hotstate-1]
        else:
            time += cold[programs[i]-1]
            hotstate = programs[i]
    return time

for i in range(1, len(lines), 4):
    n, k = map(int, lines[i].split())
    programs = list(map(int, lines[i + 1].split()))
    cold = list(map(int, lines[i + 2].split()))
    hot = list(map(int, lines[i + 3].split()))
    @lru_cache(None)
    def recur(j, a_hot, b_hot):
        if j == n:
            return 0
        if programs[j] in (a_hot, b_hot):
            return hot[programs[j]-1] + recur(j + 1, a_hot, b_hot)
        a = cold[programs[j]-1] + recur(j + 1, a_hot, programs[j])
        b = cold[programs[j]-1] + recur(j + 1, programs[j], b_hot)
        return min(a, b)
    print(recur(0, 0, 0))


            
