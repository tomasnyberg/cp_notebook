import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

# 0 == clockwise
# 1 == counter-clockwise
# 2 == either
def possible(n, players, dist, dir):
    possible = set()
    for start in players:
        if dir in [0,2]:
            possible.add((start + dist) % n)
        if dir in [1,2]:
            possible.add((start - dist) % n)
    return possible

ii = 1
while ii < len(lines):
    n, m, x = map(int, lines[ii].split())
    x-=1
    ii += 1
    players = set([x])
    for _ in range(m):
        dist, dir = lines[ii].split()
        dir = int(dir) if dir != '?' else 2
        players = possible(n, players, int(dist), dir)
        ii+=1
    print(len(players))
    print(*list(map(lambda x: x+1, sorted(players))))

