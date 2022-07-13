import sys
from queue import deque
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    start_times = list(map(int, lines[i+1].split(" ")))
    end_times = list(map(int, lines[i+2].split(" ")))
    in_queue = deque()
    finished_by = -1
    res = []
    for j in range(len(start_times)):
        if finished_by < start_times[j]:
            res.append(end_times[j] - start_times[j])
            finished_by = end_times[j]
        else:
            res.append(end_times[j] - finished_by)
            finished_by = end_times[j]
    for x in res:
        print(x, end=" ")
    print()
    i += 3