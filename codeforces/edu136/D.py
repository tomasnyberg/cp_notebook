def solve(n, k, p):
    p = [0] + [x-1 for x in p]
    def check(h):
        d = [1] * n
        ops = 0
        for i in range(n-1, 0, -1):
            if d[i] == h and p[i] != 0:
                ops += 1
            else:
                d[p[i]] = max(d[p[i]], d[i] + 1)
        return ops <= k
    
    low, high = 1, n-1
    while low < high:
        mid = (low + high) >> 1
        if check(mid):
            high = mid
        else:
            low = mid + 1
    return low

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, k, p))
