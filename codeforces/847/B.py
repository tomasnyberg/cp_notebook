import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, s, r = map(int, line.split())
    result = [s - r]
    remaining = s - result[0]
    # find n-1 numbers between 1 and 6 such that they sum to remaining
    n-=1
    while n > 0:
        n-=1
        if remaining == n:
            result.append(1)
            remaining -= 1
        else:
            result.append(min(6, remaining - n))
            remaining -= result[-1]
    assert(sum(result) == s)
    print(*result)