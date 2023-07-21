import sys
lines = list(map(str.strip, sys.stdin.readlines()))

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    ii += 1
    best = [-1, -1]
    for i in range(n):
        a, b = map(int, lines[ii].split())
        ii+=1
        if a > 10: continue
        best = max(best, [b, i])
    print(best[1] + 1)