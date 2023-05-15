import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

for line in lines[1:]:
    n, k = map(int, line.split(" "))
    mapping = {i: n - i - 1 for i in range(n//2)}
    if k == n - 1:
        if n == 4:
            print(-1)
            continue
        mapping[n-2] = n-1
        mapping[1] = 3
        mapping[0] = n-4
        del mapping[3]
    else:
        mapping[k] = n-1
        mapping[n-k-1] = 0
        del mapping[0]
    for x in mapping:
        print(x, mapping[x])
    

