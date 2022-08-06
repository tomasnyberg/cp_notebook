import sys
from heapq import heappush, heappop
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(nums):
    hq = []
    for x in nums:
        heappush(hq, x)
    while len(hq) >= 2:
        first = heappop(hq) 
        second = heappop(hq)
        if second - first > 1:
            print("NO")
            return
        heappush(hq, first + second)
    print("YES")

for i in range(1, len(lines),2 ):
    n = int(lines[i])
    operations = n-1
    nums = list(map(int, lines[i+1].split(" ")))
    solve(nums)