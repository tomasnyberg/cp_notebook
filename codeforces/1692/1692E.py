import sys
import bisect
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for i in range(1, len(lines), 2):
    n, s = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    CSL = cum_sum(nums)
    CSR = cum_sum(list(reversed(nums)))
    total = sum(nums)
    to_remove = total - s
    if to_remove < 0:
        print(-1)
        continue
    if to_remove == 0:
        print(0)
        continue
    best = len(nums)
    for idx, x in enumerate(CSL):
        if x == to_remove:
            best = min(idx + 1, best)
            break
        withoutx = idx + bisect.bisect_left(CSR, to_remove) + 1
        withx = idx + 1 + bisect.bisect_left(CSR, to_remove - x) + 1
        best = min(withx, withoutx, best)
    print(best)
        
