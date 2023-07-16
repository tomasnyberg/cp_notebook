import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# dirs in 4 directions
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def any_near(vi, vj, friends):
    for x, y in friends:
        if manhattan((vi, vj), (x, y)) == 1:
            return False
    return True

ii = 1
while ii < len(lines):
    n, m, k = list(map(int, lines[ii].split()))
    corners = [(1, 1), (1, m), (n, 1), (n, m)]
    ii += 1
    vi, vj = list(map(int, lines[ii].split()))
    ii += 1
    friends = []
    for _ in range(k):
        a, b = list(map(int, lines[ii].split()))
        friends.append((a, b))
        ii += 1
    if any((vi, vj) == (x, y) for x, y in friends):
        print("NO")
        continue
    if all(manhattan((vi, vj), (x, y)) % 2 == 1 for x, y in friends):
        print("YES")
        continue
    else:
        print("NO")