import sys
import bisect
lines = list(map(str.strip, sys.stdin.readlines()))

MOD = 10**9 + 7

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split(" "))
    nums = list(map(int, lines[ii+1].split(" ")))
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    nums = list(sorted(set(nums)))
    left = 0
    right = 0
    multiplier = 1
    result = 0
    while right < len(nums):
        multiplier *= counts[nums[right]]
        if right - left + 1 == k:
            if nums[right] - nums[left] == right - left:
                result += multiplier
                result %= MOD
            multiplier //= counts[nums[left]]
            left += 1
        right += 1
    print(result)

        
    
    # print(nums)