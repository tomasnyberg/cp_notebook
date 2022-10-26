import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def costs(line):
    sheep_seen = 0
    running = 0
    res = []
    for c in line:
        if c == '*':
            sheep_seen += 1
        else:
            running += sheep_seen
        res.append(running)
    return res

for line in lines[2::2]:
    from_left = costs(line)
    from_right = costs(line[::-1])
    from_right.reverse()
    res = 10**25
    for i in range(len(from_left)):
        res = min(res, from_left[i] + from_right[i])
    print(res)
            