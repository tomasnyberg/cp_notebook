import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def validpartition(nums, target):
    curr = 0
    currlen = 0
    partitions = 0
    longest = 0
    for x in nums:
        curr += x
        currlen += 1
        if curr == target:
            longest = max(longest, currlen)
            curr = 0
            currlen = 0
            partitions += 1
    return [partitions, longest]
        

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    result = len(nums)
    total = sum(nums)
    for i in range(1, int(math.sqrt(total))+3):
        if total % i == 0:
            partitions, longest = validpartition(nums, total // i)
            if partitions != i: continue
            result = min(result, longest)
    print(result)