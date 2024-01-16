import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    xs = list(map(int, lines[ii+1].split()))
    ys = list(map(int, lines[ii+2].split()))
    xs.sort()
    ys.sort()
    xs = deque(xs)
    ys = deque(ys)
    # print(xs)
    # print(ys)
    result = 0
    while xs:
        bigdiff = xs[-1] - ys[0]
        smalldiff = ys[-1] - xs[0]
        if bigdiff > smalldiff:
            result += bigdiff
            xs.pop()
            ys.popleft()
        else:
            result += smalldiff
            xs.popleft()
            ys.pop()
    print(result)


