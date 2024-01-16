import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    have = lines[ii+1]
    want = lines[ii+2]
    needed = 0
    cats = 0
    for x, y in zip(have, want):
        if x == y:
            continue
        if x == '0':
            needed += 1
        else:
            cats += 1
    result = 0
    if cats > needed:
        result += cats - needed
    else:
        temp = needed - cats
        result += needed - cats
        needed -= temp
    result += needed
    print(result)
