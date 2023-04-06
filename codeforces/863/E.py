import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(x):
    x = str(x)[::-1]
    result = 0
    for i in range(len(x)):
        inted = int(x[i]) if x[i] < '4' else int(x[i]) -1
        result += inted * 9**i
    return result

def bs(n):
    l, r = 0, 10**17
    while l < r:
        mid = (l + r) // 2
        if check(mid) < n:
            l = mid + 1
        else:
            r = mid
    l = list(str(l))
    for i in range(len(l)):
        if l[i] == '4':
            l[i] = '3'
    return ''.join(l)

for line in lines[1:]:
    n = (line)
    print(bs(int(n)))
