import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 2):
    n, k, q = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    result = 0
    subs = []
    curr = []
    for x in a:
        if x > q:
            if len(curr) >= k:
                subs.append(curr)
            curr = []
        else:
            curr.append(x)
    if len(curr) >= k:
        subs.append(curr)
    for sub in subs:
        for i in range(len(sub)-k+1):
            result += len(sub)-i-k+1
    print(result)