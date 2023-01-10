import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n = int(lines[i])
    matrix = [lines[i+1], lines[i+2]]
    bad = False
    sums = []
    for j in range(n):
        tot = 0
        for k in range(2):
            tot += 1 if matrix[k][j] == 'B' else 0
        if tot == 0:
            bad = True 
        sums.append(tot)
    for j in range(1, n - 1):
        if sums[j] == 2 and sums[j-1] == 1 and sums[j+1] == 1:
            bad = True
    for j in range(n-1):
        if sums[j] == 1 and sums[j+1] == 1:
            if matrix[j][0] != matrix[j+1][0]:
                bad = True
    print("YES" if not bad else "NO")

    
    