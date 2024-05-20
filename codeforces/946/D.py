import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def do_move(a, move):
    return [a[0] + move[0], a[1] + move[1]]


for line in lines[2::2]:
    heli = [0, 0]
    rover = [0, 0]
    moves = []
    mapped = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
    for c in line:
        moves.append(mapped[c])
    # heli = do_move(heli, moves[0])
    # rover = do_move(rover, moves[1])
    # moves = moves[2:]
    moved = [False, False]
    result = []
    for move in moves:
        # print(heli, rover)
        smallest_dist = [10**10, -1]
        for i, (mover, other) in enumerate([[heli, rover], [rover, heli]]):
            temp = do_move(mover, move)
            dist = manhattan(temp, other)
            if dist < smallest_dist[0] or dist == smallest_dist[0] and not moved[i]:
                smallest_dist = [dist, i]
        if smallest_dist[1] == 0:
            heli = do_move(heli, move)
            moved[0] = True
            result.append('H')
        else:
            moved[1] = True
            rover = do_move(rover, move)
            result.append('R')
    if heli == rover and all(moved):
        print(''.join(result))
    else:
        print("NO")
