import sys
from queue import deque
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n, m = map(int, lines[i].split(" "))
    memory = list(map(int, lines[i+1].split(" ")))
    convenience = list(map(int, lines[i+2].split(" ")))
    if sum(memory) < m:
        print(-1)
        continue
    xs = []
    for j in range(len(memory)):
        xs.append((memory[j], memory[j]/convenience[j], convenience[j]))
    xs.sort(key=lambda x: (-x[1], x[2]))
    dq = deque(xs)
    gotten = 0
    result = 0
    while gotten < m:
        inc, _, con = dq.popleft()
        gotten += inc
        result += con
    print(xs)
    print(result)