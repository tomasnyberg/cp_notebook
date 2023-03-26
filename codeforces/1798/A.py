import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def try_swap(a, b):
    a = a[:]
    b = b[:]
    abig = a[-1]
    bbig = b[-1]
    for i in range(len(a)-1):
        if a[i] > abig:
            a[i], b[i] = b[i], a[i]
        if b[i] > bbig:
            a[i], b[i] = b[i], a[i]
    return max(a) == abig and max(b) == bbig

i = 1
for i in range(1, len(lines), 3):
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    first = try_swap(a, b)
    a[-1], b[-1] = b[-1], a[-1]
    second = try_swap(a, b)
    if first or second:
        print("YES")
    else:
        print("NO")