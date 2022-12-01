import sys
lines = list(map(str.strip, sys.stdin.readlines()))

insts = []
for line in lines:
    insts.append((line[0], int(line[1:])))

def solve(part_one):
    def add_right(c, num, xs):
        i = 1 if c in ['N', 'S'] else 0
        sign = 1 if c in ['N', 'E'] else -1
        xs[i] += sign * num
    def right_direction(dir):
        i = 1 if dir in [1, 3] else 0
        sign = 1 if dir in [0, 3] else -1
        return (i, sign)
    dir = 0
    pos = [0, 0]
    wp = [10, 1]
    for c, num in insts:
        if c in ['N', 'S', 'E', 'W']:
            if part_one:
                add_right(c, num, pos)
            else:
                add_right(c, num, wp)
        elif c in ['R', 'L']:
            add = 1 if c == 'R' else -1
            dir = (dir + add * num // 90) % 4
            if num == 90:
                wp = [wp[1] * add, wp[0] * -add]
            elif num == 180:
                wp = [wp[0] * -1, wp[1] * -1]
            elif num == 270:
                wp = [wp[1] * -add, wp[0] * add]
        else:
            
            if part_one:
                i, sign = right_direction(dir)
                pos[i] += sign * num
            else:
                pos[0] += num*wp[0]
                pos[1] += num*wp[1]
    return abs(pos[0]) + abs(pos[1])

print("Part one:", solve(True))
print("Part two:", solve(False))