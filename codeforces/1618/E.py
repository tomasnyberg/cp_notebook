import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    b = list(map(int, line.split(" ")))
    n = len(b)
    S = 2*sum(b)/(n*(n+1))
    result = [0]*n
    bad = False
    for i in range(len(b)):
        result[i] = int((S - b[i] + b[(i+n-1)%n]) // n)
        if result[i] <= 0:
            print("NO")
            bad = True
            break
    if bad: continue
    print("YES")
    print(*result)