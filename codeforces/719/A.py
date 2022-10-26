import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    prev = line[0]
    seen = set()
    bad = False
    for i in range(1, len(line)):
        if line[i] != prev:
            if line[i] in seen:
                bad = True
                break
            seen.add(prev)
            prev = line[i]
    if bad:
        print("NO")
    else:
        print("YES")