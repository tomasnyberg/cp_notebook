import sys
lines = list(map(str.strip, sys.stdin.readlines()))


dirs = [[-1,0], [1,0], [0,1], [0,-1]]
for line in lines[1:]:
    n, m, sx, sy, d = map(int, line.split(" "))
    if (sx - d <= 1 and sy - d <= 1) or (sx + d >= n and sy + d >= m) or (abs(n-sx) + abs(m-sy)) <= d or (sx + d >= n and sx - d <= 1) or (sy + d >= m and sy - d <= 1):
        print(-1)
    else:
        print(n- 1 + m - 1)
