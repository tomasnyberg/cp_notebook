import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    a, b, c = map(int, line.split())
    best = [10**9, -1]
    for i in range(11):
        dist = abs(i - a) + abs(i - b) + abs(i - c)
        if dist < best[0]:
            best = [dist, i]
    print(best[0])
