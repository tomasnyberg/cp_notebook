import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, k = map(int, lines[i].split())
    i+=1
    segments = []
    for _ in range(n):
        l, r = map(int, lines[i].split())
        i+=1
        if not l <= k <= r: continue
        segments.append((l, r))
    counts = [0] * 51
    for fr, to in segments:
        for j in range(fr, to+1):
            counts[j] += 1
    # If counts[k] is greater than all other points
    if counts[k] > max(counts[:k] + counts[k+1:]):
        print("YES")
    else:
        print("NO")
    