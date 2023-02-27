import sys
import bisect
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
    seen = {}
    for idx, x in enumerate(programs):
        if x not in seen:
            seen[x] = []
        seen[x].append(idx)
    hotstate_a = [-1, 0]
    hotstate_b = [-1, 0]
    time = 0
    for idx, x in enumerate(programs):
        if x in [hotstate_a[0], hotstate_b[0]]:
            time += hot[x-1]
        else:
            if hotstate_a[0] == -1:
                hotstate_a = [x, idx]
                time += cold[x-1]
                continue
            if hotstate_b[0] == -1:
                hotstate_b = [x, idx]
                time += cold[x-1]
                continue
            a_next = seen[hotstate_a[0]][hotstate_a[1] + 1] if hotstate_a[1] + 1 < len(seen[hotstate_a[0]]) else n
            timesave_a = 0
            if a_next != n:
                timesave_a = cold[hotstate_a[0]-1] - hot[hotstate_a[0]-1]
            b_next = seen[hotstate_b[0]][hotstate_b[1] + 1] if hotstate_b[1] + 1 < len(seen[hotstate_b[0]]) else n
            timesave_b = 0
            if b_next != n:
                timesave_b = cold[hotstate_b[0]-1] - hot[hotstate_b[0]-1]
            time_taken_a = calculate_cost(programs, idx, a_next, hot, cold)
            time_taken_b = calculate_cost(programs, idx, b_next, hot, cold)
            if time_taken_a + timesave_a < time_taken_b + timesave_b:
                time += cold[x-1]
                hotstate_b = [x, idx]
            else:
                time += cold[x-1]
                hotstate_a = [x, idx]
    print(time)



            
