import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def layer(x, y, n):
    return max(abs(x - (n + 1)), abs(y - (n + 1)))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    a = []
    added = False
    for x in nums:
        if not a:
            a.append(x)
        else:
            if a[-1] > x:
                if len(a) >= 3 and a[-2] >= a[-1]:
                    a[-1] = x
                else:
                    a.append(x)
                    added = True
                a.append(x)
            else:
                a.append(x)
    if not added:
        if len(a) >= 2 and a[0] < a[1]:
            a.insert(0, a[0])
        else:
            a.append(a[-1])
    print(*a)
        


