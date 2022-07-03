import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 2
while i < len(lines):
    n, m = map(int, lines[i].split(" "))
    points = []
    scores = []
    for j in range(i+1, i+1+m):
        x, score = map(int, lines[j].split(" "))
        points.append([x, score, j-i])
    i += m + 2
    points.sort(key = lambda x: x[1])
    points = points[:n*2]
    points.sort(key = lambda x: x[0])
    left = 0
    right = len(points) - 1
    print(sum(list(map(lambda x: x[1], points))))
    while left < right:
        print(points[left][2], points[right][2])
        left += 1
        right -= 1
    print()