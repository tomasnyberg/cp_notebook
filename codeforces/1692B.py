import sys
from queue import deque
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    nums = list(map(int, lines[i+1].split(" ")))
    distinct = set(nums)
    x = len(distinct)
    if x % 2 == len(nums) % 2:
        print(x)
    else:
        print(x-1)



        

