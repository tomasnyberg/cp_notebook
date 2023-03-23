import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(l, target):
    return (l+1)**2 >= target


for line in lines[1:]:
    n = int(line)
    low = 0
    high = 10**25
    while low < high:
        mid = (low + high) >> 1
        if check(mid, n):
            high = mid
        else:
            low = mid + 1
    print(low)
