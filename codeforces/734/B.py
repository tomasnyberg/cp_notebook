import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    counts = {}
    atleasttwo = 0
    singles = 0
    for c in line:
        if c not in counts: counts[c] = 0
        counts[c] +=1
        if counts[c] == 1: singles +=1
        if counts[c] == 2:
            singles -=1
            atleasttwo += 1
    print(atleasttwo + (singles//2))

