import sys
lines = list(map(str.strip, sys.stdin.readlines()))


MOD = 10**9 + 7
def solve(n, a, b):
    a.sort()
    b.sort()
    ans = 1
    j = n - 1
    for i in range(n - 1, -1, -1):
        while j >= 0 and a[j] > b[i]:
            j -= 1
        ans *= (i - j)
        ans %= MOD
    return ans

for i in range(1, len(lines), 3):
    n = int(lines[i])
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    print(solve(n, a, b))