import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 2
while i < len(lines):
    n, m = map(int, lines[i].split(" "))
    points = []
    scores = []
    for j in range(i+1, i+1+m):
        x, score = map(int, lines[j].split(" "))
        points.append([x, score])
        scores.append(score)
    i += m + 2
    points.sort(key = lambda x: x[0])
    scores.sort()
    print(sum(scores[:n*2]))
    print(points)