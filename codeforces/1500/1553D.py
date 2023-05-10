import sys
lines = list(map(str.strip, sys.stdin.readlines()))


for i in range(1, len(lines), 2):
    a, b = lines[i], lines[i+1]
    a = list(a)
    b = list(b)
    while a and b:
        if a[-1] == b[-1]:
            a.pop()
            b.pop()
        else:
            a.pop()
            if a:
                a.pop()
    print("YES" if not b else "NO")

