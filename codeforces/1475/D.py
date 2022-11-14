import sys
from queue import deque
from heapq import heappop, heappush
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
        xs.append((memory[j], memory[j]/convenience[j], convenience[j], j))
    xs.sort(key=lambda x: (-x[1], x[2]))
    dq = deque(xs)
    gotten = 0
    result = 0
    taken = set()
    hq = []
    for j in range(len(memory)):
        # if convenience[j] == 2: continue
        hq.append((-memory[j], convenience[j], j))
    while gotten < m:
        good = False
        if dq[0][0] + gotten < m:
            while hq and -hq[0][0] + gotten >= m:
                mem, con, idx = heappop(hq)
                if idx in taken: continue 
                result += con
                good = True
                break
        if good:
            break
        inc, _, con, j = dq.popleft()
        gotten += inc
        result += con
        taken.add(j)
    # print(xs)
    print(result)