import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(str):
    split = list(filter(lambda x: len(x) > 0, str.split("W")))
    for part in split:
        if len(part) == 1:
            print("NO")
            return
        bcount = 0
        rcount = 0
        for c in part:
            if c == 'B':
                bcount+=1
            else:
                rcount +=1
        if rcount == 0 or bcount == 0:
            print("NO")
            return
    print("YES")

for i in range(2, len(lines), 2):
    str = lines[i]
    solve(str)
