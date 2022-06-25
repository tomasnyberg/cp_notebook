import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    biggest = max(nums)
    cs = cum_sum(nums)
    special = set()
    for k in range(1, len(nums)):
        a = 0
        b = k
        total = cs[k-1]
        while(b < len(nums)):
            total += nums[b] 
            if total <= biggest:
                special.add(total)
            total -= nums[a]
            a += 1
            b += 1
    result = 0
    for num in nums:
        if num in special:
            result += 1
    print(result)
