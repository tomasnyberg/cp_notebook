import sys
lines = list(map(str.strip, sys.stdin.readlines()))

#4 dirs 
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def brute_force(n, m, robots, vertical, horizontal, visited):
    if (vertical, horizontal) in visited:
        return False
    if (1, 1) in robots:
        return True
    visited.add((vertical, horizontal))
    for dx, dy in dirs:
        if all(1 <= r[0] + dx <= n and 1 <= r[1] + dy <= m for r in robots):
            new_robots = {(r[0] + dx, r[1] + dy) for r in robots}
            if brute_force(n, m, new_robots, vertical + dx, horizontal + dy, visited):
                return True
    return False

i = 1
while i < len(lines):
    n, m = map(int, lines[i].split())
    i+=1
    robots = set()
    for r in range(n):
        for c in range(m):
            if lines[i][c] == 'R':
                robots.add((r+1, c+1))
        i+=1
    visited = set()
    if brute_force(n, m, robots, 0, 0, visited):
        print('YES')
    else:
        print("NO")