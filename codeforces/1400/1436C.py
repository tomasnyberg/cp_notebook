import sys
lines = list(map(str.strip, sys.stdin.readlines()))

MOD = 10**9 + 7

def bs(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left > 0 and a[left - 1] == x

def factorial(x):
    ans = 1
    for i in range(1, x + 1):
        ans *= i
        ans %= MOD
    return ans

for line in lines:
    n, x, pos = map(int, line.split())
    low = 0
    high = n
    bigger = n - x
    smaller = x - 1
    ans = 1
    while low - 1 != pos:
        mid = (low + high) // 2
        if mid <= pos:
            ans *= bigger
            bigger -= 1
            low = mid + 1
        else:
            ans *= smaller
            smaller -= 1
            high = mid
    ans *= factorial(bigger + smaller)
    ans %= MOD
    print(ans)
    
