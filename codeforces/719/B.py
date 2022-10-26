import sys
lines = list(map(str.strip, sys.stdin.readlines()))

counts = {}
for line in lines[1:]:
    x = int(line)
    res = 0
    for d in range(1, 10):
        curr = 0
        for k in range(9):
            curr += 10**k
            if d*curr <= x:
                res += 1
    print(res)

    
