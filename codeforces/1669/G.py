import sys
lines = list(map(str.strip, sys.stdin.readlines()))

r = 1
while r < len(lines):
    n, m = map(int, lines[r].split(" "))
    start = []
    r+=1
    result = [['.' for _ in range(m)] for _ in range(n)]
    highest = [0] * m
    while n > 0:
        start.append(lines[r])
        r+=1
        n-=1
    for i in range(len(result) - 1, -1, -1):
        for j in range(len(result[0])):
            if start[i][j] == 'o':
                result[i][j] = 'o'
                highest[j] = len(result) - i
            if start[i][j] == '*':
                result[len(result) - highest[j] - 1 ][j] = '*'
                highest[j] +=1
    for str in result:
        for c in str:
            print(c, end="")
        print()