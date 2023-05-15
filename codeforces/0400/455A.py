import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))

def optimal(xs):
    @lru_cache(None)
    def recur(i, prevtaken):
        if i == len(xs):
            return 0
        if prevtaken:
            return recur(i+1, False)
        else:
            return max(xs[i] + recur(i+1, True), recur(i+1, False))
    return recur(0, False)

def optimal_iter(xs):
    n = len(xs)
    dp = [0] * (n + 1) # dp[i] represents the optimal solution for xs[0:i]

    for i in range(1, n + 1):
        not_take = dp[i - 1]
        take = xs[i - 1] + (dp[i - 2] if i - 2 >= 0 else 0)
        dp[i] = max(take, not_take)

    return dp[n]


nums = list(map(int, lines[1].split(" ")))
counts = {}
for x in nums:
    counts[x] = 1 if x not in counts else counts[x] + 1
result = 0
taken = set()
for key in counts:
    if key in taken: continue
    taken.add(key)
    curr_xs = [key*counts[key]]
    ptr = key - 1
    add_behind = []
    while ptr in counts:
        taken.add(ptr)
        add_behind.append(ptr*counts[ptr])
        ptr -= 1
    curr_xs = add_behind[::-1] + curr_xs
    ptr = key + 1
    while ptr in counts:
        taken.add(ptr)
        curr_xs.append(ptr*counts[ptr])
        ptr += 1
    result += optimal_iter(curr_xs)
print(result)
    