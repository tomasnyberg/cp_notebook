import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 4):
    n, target = map(int, lines[ii].split())
    stacks = []
    stacks.append(list(map(int, lines[ii+1].split())))
    stacks.append(list(map(int, lines[ii+2].split())))
    stacks.append(list(map(int, lines[ii+3].split())))
    for xs in stacks:
        xs.reverse()
    curr = 0
    inverted = 0
    for i in range(32):
        if not (1 << i) & target:
            inverted |= (1 << i)
    # print(bin(target)[2:].zfill(33))
    # print(bin(inverted)[2:].zfill(33))
    while curr != target:
        if all(len(xs) == 0 for xs in stacks):
            break
        for i, xs in enumerate(stacks):
            if not xs: continue
            if inverted & xs[-1]:
                stacks[i] = []
                continue
            else:
                curr |= xs.pop()
    print("Yes" if curr == target else "No")


             
