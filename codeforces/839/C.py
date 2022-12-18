import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    k, n = map(int, line.split())
    gap = 1
    curr = 1
    result = [1]
    k-=1
    while k:
        if curr + gap <= n - k + 1:
            curr += gap
            result.append(curr)
        else:
            result.append(result[-1] + 1)
        gap += 1
        k-=1
    print(*result)