import sys
lines = list(map(str.strip, sys.stdin.readlines()))

moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
for line in lines[1:]:
    a, b = map(int, line.split())
    ans = (1, 1)
    for i in range(1, a+1):
        for j in range(1, b+1):
            if all(( i+dx < 1 or i+dx > a or j+dy < 1 or j+dy > b for dx, dy in moves )):
                ans = (i, j)
                break
    print(*ans)
