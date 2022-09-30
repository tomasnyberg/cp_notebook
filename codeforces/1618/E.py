import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    b = list(map(int, line.split(" ")))
    n = len(b)
    S = 2*sum(b)/(n*(n+1))
    d = (n*(n+1)) // 2
    if sum(b) % d != 0:
        print("NO")
        continue
    result = [0]*n
    bad = False
    for i in range(len(b)-1,-1,-1):
        res = int(b[i] - b[(i+1)%n] + S)
        if res <= 0 or res%n != 0:
            print("NO")
            bad = True
            break
        result[(i+1)%n] = res//n
    if bad: continue
    print("YES")
    print(*result)