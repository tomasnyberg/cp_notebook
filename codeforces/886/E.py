import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for ii in range(1, len(lines), 2):
    n, c = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    def check(mid):
        total = 0
        for x in a:
            total += (x + mid)**2
            if total > c:
                return False
        return total <= c
    low = 0
    high = 10**18
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            low = mid + 1
        else:
            high = mid
    print((low - 1) // 2)

