import sys
lines = list(map(str.strip, sys.stdin.readlines()))

insts = []
for line in lines:
    insts.append((line[0], int(line[1:])))

def solve(part_one):
    dir = 0
    pos = [0, 0]
    wp = [10, 1]
    for c, num in insts:
        if c == 'N':
            pos[1] += num
            wp[1] += num
        elif c == 'S':
            pos[1] -= num
            wp[1] -= num
        elif c == 'E':
            pos[0] += num
            wp[0] += num
        elif c == 'W':
            pos[0] -= num
            wp[0] -= num
        elif c in ['R', 'L']:
            add = 1 if c == 'R' else -1
            if num == 90:
                dir = (dir + add) % 4
                wp = [wp[1] * add, wp[0] * -add]
            elif num == 180:
                dir = (dir + 2*add) % 4
                wp = [wp[0] * -1, wp[1] * -1]
            elif num == 270:
                dir = (dir + 3*add) % 4
                wp = [wp[1] * -add, wp[0] * add]
        else:
            if part_one:
                if dir == 0:
                    pos[0] += num
                elif dir == 1:
                    pos[1] -= num
                elif dir == 2:
                    pos[0] -= num
                else:
                    pos[1] += num
            else:
                pos[0] += num*wp[0]
                pos[1] += num*wp[1]
    return abs(pos[0]) + abs(pos[1])

print("Part one:", solve(True))
print("Part two:", solve(False))