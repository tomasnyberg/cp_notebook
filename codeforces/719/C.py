import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    x = int(line)
    if x == 2:
        print(-1)
        continue
    matrix = [[0 for _ in range(x)] for _ in range(x)]
    high = x**2
    low = 1
    count = 0
    for i in range(x): 
        for j in range(x):
            if count % 2 == 0:
                matrix[i][j] = low
                low += 1
            if count % 2 == 1:
                matrix[i][j] = high
                high -= 1
            count += 1
    temp = matrix[0][0]
    matrix[0][0] = matrix[-1][-1]
    matrix[-1][-1] = temp
    for xs in matrix:
        print(*xs)
