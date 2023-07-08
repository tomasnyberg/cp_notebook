import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def optimal(problems, time):
    problems.sort()
    penalty = 0
    solved = 0
    curr_time = 0
    for p in problems:
        if curr_time + p <= time:
            curr_time += p
            penalty += curr_time
            solved += 1
    return [solved, penalty]

ii = 1
while ii < len(lines):
    n, m, h = map(int, lines[ii].split())
    solve_times = []
    ii+=1
    for _ in range(n):
        nums = (list(map(int, lines[ii].split())))
        solve_times.append(optimal(nums, h))
        ii+=1
    solve_times = list(sorted(enumerate(solve_times), key=lambda x: (x[1][0], -x[1][1]), reverse=True))
    for i in range(len(solve_times)):
        if solve_times[i][0] == 0:
            print(i+1)
            break
    
