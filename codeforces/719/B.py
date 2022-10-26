import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    x = int(line)
    n = len(str(x))
    res = 0
    res += (n-1)*9
    res += int(line[0])-1
    for c in line[1:]:
        if c == line[0]: continue
        if c < line[0]: break
        if c > line[0]: 
            res += 1
            break
    if all (c == line[0] for c in line[1:]):
        res += 1
    print(res)
