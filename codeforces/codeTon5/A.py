import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

for ii in range(1, len(lines), 3):
    a = list(map(int, lines[ii+1].split()))
    b = list(map(int, lines[ii+2].split()))
    a.sort()
    b.sort()
    a = deque(a)
    b = deque(b)
    turn = 1
    while a and b:
        first = -1
        second = -1
        if turn:
            first = a.popleft()
            second = b.pop()
        else:
            first = b.popleft()
            second = a.pop()
        if first - second > 0:
            a.appendleft(first - second)
        if second - first > 0:
            b.appendleft(second - first)
    if not a and not b:
        print("Draw")
        continue
    if a and not b:
        print("Tsondu")
    else:
        print("Tenzing")


    
    