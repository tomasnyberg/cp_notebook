import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def operation(a, b):
    c = []
    for x, y in zip(a,b):
        c.append(abs(x-y))
    return b, c

for ii in range(1, len(lines), 3):
    a = list(map(int, lines[ii+1].split()))
    b = list(map(int, lines[ii+2].split()))
    for i in range(50):
        print("iteration", i)
        print(a)
        print(b)
        a, b = operation(a, b)
    # print("\n\n\n")