import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
MOD = 10**9+7

# for some 1-index i, everything SMALLER than it doesn't matter.
# start with an empty set, then

#1,0 {}
#2,3 {1, 2, 4} -> {0, 1, 2} -> 3
#3,2 {1, 2, 4} -> {0, 1} -> 2
#4,2 {1, 2, 4} -> {0, 1} -> 2
#5,2 {1, 2, 4, 5} -> {0, 1} -> 2
#6,1 {1, 2, 4, 5} -> {0} -> 1


def build_tightest(n, nums):
    tightest = [-1] * n
    # klogk
    for k in range(1, n+1):
        for chunk_index in range(nums[k-1]):
            chunk_left = chunk_index * k
            chunk_right = min(chunk_left + k - 1, n - 1)
            tightest[chunk_right] = max(tightest[chunk_right], chunk_left)
    return tightest

def build_jump_limits(n, tightest, positions):
    jump_limit = [0] * len(positions)
    r = 0
    for i, x in enumerate(positions):
        if r < x:
            r = x
        while r<n and tightest[r] <= x:
            r+=1
        jump_limit[i] = r
    return jump_limit

for l in lines[2::2]:
    nums = list(map(int, l.split()))
    n = len(nums)
    line = [0] * (n+1)
    for i, x in enumerate(nums):
        divisor = i+1
        forbidden_low = x * divisor
        forbidden_high = x * divisor + divisor - 1
        if forbidden_low >= len(line):
            continue
        forbidden_high = min(n-1, forbidden_high)
        line[forbidden_low] += 1
        line[forbidden_high+1] -= 1 
    cover = []
    running = 0
    for x in line:
        running += x
        cover.append(running)
    cover.pop()
    result = []
    for i, x in enumerate(cover):
        if not x and i < n:
            result.append(i)
    tightest = build_tightest(n, nums)
    positions = [-1] + result
    jump_limits = build_jump_limits(n, tightest, positions)
    m = len(positions)
    dp = [0]*m
    pfs = [0] * (m+1)
    dp[0] = 1
    pfs[1] = 1
    result = 1 if jump_limits[0] == n else 0
    left = 0
    for i, x in enumerate(positions):
        if i == 0:
            continue
        while jump_limits[left] < x:
            left += 1
        dp[i] = (pfs[i] - pfs[left]) % MOD
        pfs[i+1] = (pfs[i] + dp[i]) % MOD
        if jump_limits[i] == n:
            result = (result + dp[i]) % MOD
    print(result)
    # print(len(result))
    # print(*result)


