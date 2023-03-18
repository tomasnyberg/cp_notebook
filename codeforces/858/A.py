import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b, c, d = map(int, line.split())
    if b > d:
        print(-1)
        continue
    result = 0
    result += abs(d - b)
    a += result
    b += result
    if a < c:
        print(-1)
        continue
    result += abs(c - a)
    print(result)
    
    