MOD = 998244353

def count_divisors(n):
    """Count the number of divisors of n."""
    count = 1
    i = 2
    while i * i <= n:
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i
        count *= exp + 1
        i += 1
    if n > 1:
        count *= 2
    return count

def solve():
    l, r = map(int, input().split())
    if l == r:
        print("1 1")
    else:
        count = count_divisors(l)
        print((r // l) + (r % l != 0), count % MOD)

t = int(input())
for _ in range(t):
    solve()