import sys
from queue import deque
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for i in range(1, len(lines), 3):
    n, m = map(int, lines[i].split(" "))
    memory = list(map(int, lines[i+1].split(" ")))
    convenience = list(map(int, lines[i+2].split(" ")))
    if sum(memory) < m:
        print(-1)
        continue
    ones = []
    twos = []
    for j in range(len(memory)):
        if convenience[j] == 1:
            ones.append(memory[j])
        else:
            twos.append(memory[j])
    ones.sort(key=lambda x: -x)
    twos.sort(key=lambda x: -x)
    dq1 = deque(ones)
    dq2 = deque(twos)
    gotten = 0
    result = 0
    while gotten < m:
        if not dq1:
            while gotten < m:
                result+=2
                gotten += dq2.popleft()
            break
        elif not dq2:
            while gotten < m:
                result+=1
                gotten += dq1.popleft()
            break
        if dq1[0] + gotten >= m:
            result += 1
            break
        if len(dq1) >= 2 and dq1[0] + dq1[1] >= dq2[0]:
            result += 1
            gotten += dq1.popleft()
        else:
            result += 2
            gotten += dq2.popleft()
    print(result)