import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    moves = line
    x, y = 0, 0
    visited = set()
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        visited.add((x, y))
    print("YES" if (1,1) in visited else "NO")
