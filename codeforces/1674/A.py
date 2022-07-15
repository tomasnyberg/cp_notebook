import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(x, y):
    for b in range(1, 101):
        for a in range(1, 101):
            if b**a > 100:
                break
            if x * (b**a) == y:
                print(a, b)
                return
    print(0, 0)


for line in lines[1:]:
    x, y = map(int, line.split(" "))
    solve(x, y)