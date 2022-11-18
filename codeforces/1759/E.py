import sys
from queue import deque
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, power = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort()
    result = 0
    for serums in [deque([2,2,3]), deque([3,2,2]), deque([2,3,2])]:
        currpow = power
        score = 0
        dq = deque(nums)
        while dq:
            if currpow > dq[0]:
                score += 1
                currpow += dq.popleft() // 2
            else:
                if not serums:
                    break
                currpow *= serums.popleft()
        result = max(result, score)
    print(result)