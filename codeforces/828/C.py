import sys, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, now = lines[i].split(" ")
    s = lines[i+1]
    if now == 'g':
        print(0)
        continue
    longests = {'r': 0, 'y':0}
    greens = []
    for j in range(len(s)):
        if s[j] == 'g':
            greens.append(j)
    for idx, c in enumerate(s):
        if c == 'g' or c != now: continue
        if idx > greens[-1]:
            # this could be wrong but i think it's right
            longests[c] = max(longests[c], len(s) - idx + greens[0])
            continue
        # print(idx, c)
        nextgreen = greens[bisect.bisect_right(greens, idx)]
        assert(nextgreen > idx)
        longests[c] = max(longests[c], nextgreen - idx)
    print(longests[now])
    # print(greens)