import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(a, b):
    lowest_bad = -1
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            # pop off elements off of a and add them to b until a[i] != a[i+1]
            while len(a) > i+1:
                b.append(a.pop())
            break
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            # pop off elements off of b and add them to a until b[i] != b[i+1]
            while len(b) > i+1:
                a.append(b.pop())
            break
    # print(a)
    # print(b)
    return check_good(a, b)

def check_good(a, b):
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            return False
    for i in range(1, len(b)):
        if b[i] == b[i-1]:
            return False
    return True




for i in range(1, len(lines), 3):
    a = list(lines[i+1])
    b = list(lines[i+2])
    print("YES" if check(a, b) else "NO")
    