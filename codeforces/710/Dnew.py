from heapq import heappop, heappush
import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    counts = {}
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
    count_key = [(counts[key], key) for key in counts]
    hq = []
    for count, key in count_key:
        heappush(hq, -count)
    while len(hq) > 1:
        a = -heappop(hq)
        b = -heappop(hq)
        a -= 1
        b -= 1
        if a: heappush(hq, -a)
        if b: heappush(hq, -b)
    print(0 if not hq else -hq[0])

