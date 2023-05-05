import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    mbs = []
    result = 10**9
    onesmallest = 10**9
    twosmallest = 10**9
    for _ in range(n):
        m, b = lines[i].split(" ")
        m = int(m)
        b = int(b, 2)
        if b == 3:
            result = min(result, m)
        elif b == 2:
            twosmallest = min(twosmallest, m)
        elif b == 1:
            onesmallest = min(onesmallest, m)
        else:
            x = 1
        i+=1
    result = min(result, onesmallest + twosmallest) 
    print(result if result < 10**9 else -1)
    