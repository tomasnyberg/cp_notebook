import sys
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    hq = []
    seen = set()
    counts = {}
    for num in nums:
        counts[num] = 1 if num not in counts else counts[num] + 1
        if num in seen:
            heappush(hq, -num)
        seen.add(num)
    # Take care of 0
    dp = [0]
    print(hq)
    print(counts[0], end=" ")
    bad = False
    for i in range(1, len(nums)+1):
        if bad:
            print(-1, end=" ")
            continue
        if i-1 in seen:
            dp.append(dp[i-1])
        else:
            if not hq or -hq[0] >= i: 
                bad = True
                print(-1, end=" ")
                continue
            biggest = -heappop(hq)
            seen.add(i-1)
            dp.append(i-1 - biggest + dp[i-1])
        print((counts[i] if i in counts else 0) + dp[i], end=" ")
    print()
    print(dp)

