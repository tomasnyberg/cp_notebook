import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

for line in lines[2::2]:
    s = list(line.lower())
    s.reverse()
    for char in ['m', 'e', 'o', 'w']:
        atleastone = False
        while s and s[-1] == char:
            atleastone = True
            s.pop()
        if not atleastone:
            s = True
            break
    if not s:
        print("YES")
    else:
        print("NO")