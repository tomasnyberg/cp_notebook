import sys
lines = list(map(str.strip, sys.stdin.readlines()))

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    ii+=1
    result = 0
    for _ in range(n):
        a, b = map(int, lines[ii].split())
        if b < a:
            result += 1
        ii+=1
    print(result)