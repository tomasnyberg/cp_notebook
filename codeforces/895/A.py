import sys
import math
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    a, b, c = map(int, line.split())
    a, b = max(a, b), min(a,b)
    result = 0
    while a > b:
        a -= c
        b += c
        result +=1
    print(result)
