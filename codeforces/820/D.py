import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from queue import deque

for i in range(1, len(lines), 3):
    n = int(lines[i])
    x = list(map(int, lines[i+1].split(" ")))
    y = list(map(int, lines[i+2].split(" ")))
    remaining = [have - want for want, have in zip(x, y)]
    remaining.sort()
    remaining = deque(remaining)
    result = 0
    while len(remaining) > 1:
        if remaining[0] + remaining[-1] < 0:
            remaining.popleft()
        else:
            remaining.pop()
            remaining.popleft()
            result += 1
    print(result)