import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# Write a function, that given a point on a plane and a direction, returns true if it is 
# possible to reach the given end point.
def reachable(i, j, iend, jend, dir):
    di = iend - i
    dj = jend - j
    if abs(di) == abs(dj):
        # Check if di and dir[0] have the same parity, and dj and dir[1] have the same parity
        return (di * dir[0] > 0) and (dj * dir[1] > 0)
    return False

dir_map = {"DL": (1, -1), "DR": (1, 1), "UL": (-1, -1), "UR": (-1, 1)}
for line in lines[1:]:
    n, m, istart, jstart, iend, jend, dir = line.split()
    n, m, istart, jstart, iend, jend = map(int, (n, m, istart, jstart, iend, jend))
    dir = dir_map[dir]
    i, j = istart, jstart
    if istart == iend and jstart == jend:
        print(0)
        continue
    # Find the intersection with column 1, row 1, column m, row n
    good = False
    cornerdirs  = {(1, 1):(1,1), (1, m):(1,-1), (n, 1):(-1,1), (n, m):(-1,-1)}
    seen = set()
    moves = 0
    while True:
        # Check if iend, jend is reachable with our current direction
        if (i, j) in seen:
            break
        seen.add((i, j))
        if (i, j) in cornerdirs and dir != cornerdirs[(i, j)]:
            moves += 1
            dir = cornerdirs[(i, j)]
        if reachable(i, j, iend, jend, dir):
            good = True
            break
        until_left_wall = (1 - j) // dir[1]
        until_right_wall = (m - j) // dir[1]
        until_bottom_wall = (n - i) // dir[0]
        until_top_wall = (1 - i) // dir[0]
        candidates = [(until_left_wall, 1, "LEFTWALL"), (until_right_wall, 1, "RIGHTWALL"), (until_bottom_wall, 0, "BOTTOMWALL"), (until_top_wall, 0, "TOPWALL")]
        candidates = list(filter(lambda x: x[0] > 0, candidates))
        candidates.sort(key=lambda x: x[0])
        i += candidates[0][0] * dir[0]
        j += candidates[0][0] * dir[1]
        dir = list(dir)
        dir[candidates[0][1]] *= -1
        dir = tuple(dir)
        if (i, j) == (iend, jend):
            good = True
            break
        moves += 1
        # print(i,j, dir)
    print(moves if good else -1)
