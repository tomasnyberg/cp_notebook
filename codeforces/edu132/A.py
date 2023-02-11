import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    x = int(lines[i])
    doors = list(map(int, lines[i+1].split()))
    visited = 0
    x -= 1
    for i in range(len(doors)):
        doors[i] -= 1
    while x != -1:
        x = doors[x]
        visited += 1
    print("YES" if visited == len(doors) else "NO")