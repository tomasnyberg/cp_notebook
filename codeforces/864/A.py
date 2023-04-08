import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def block_off(x, y,n,m):
    result = 4
    if x == 1 or x == n:
        result -= 1
    if y == 1 or y == m:
        result -= 1
    return result


for i in range(1, len(lines),2):
    n, m = map(int, lines[i].split())
    x1, y1, x2, y2 = map(int, lines[i+1].split())
    print(min(block_off(x1, y1,n,m), block_off(x2, y2,n,m)))
    