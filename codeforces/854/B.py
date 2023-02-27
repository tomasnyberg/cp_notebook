import sys, math
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))

def reduce_all(nums, target):
    nums_copy = nums[:]
    # Get one index of nums which equals target
    ioftarget = -1
    ans = []
    for i in range(len(nums)):
        if nums[i] == target:
            ioftarget = i
            break
    for i in range(len(nums_copy)):
        while nums_copy[i] > target:
            nums_copy[i] = math.ceil(nums_copy[i] / target)
            ans.append((i+1, ioftarget+1))
    if all(x == target for x in nums_copy):
        print(nums_copy)
        return ans
    else:
        return False
    
def find_all(nums):
    available = set(nums)
    srted = sorted(nums)
    ops = 0
    for _ in range(1):
        for x in srted:
            to_add = set()
            for y in available:
                xcopy = x
                prev = xcopy
                while True:
                    ops += 1
                    if ops % 100000 == 0:
                        print(ops)
                    xcopy = math.ceil(xcopy / y)
                    if xcopy in available or xcopy in to_add or xcopy == prev:
                        break
                    to_add.add(xcopy)
                    prev = xcopy
            available.update(to_add)
    print(available)
    print(ops)
    return available

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if 1 in nums and not all(x == 1 for x in nums):
        print(-1)
        continue
    result = []
    while True:
        biggest = [-1,-1]
        smallest = [10**10,-1]
        for j in range(len(nums)):
            if nums[j] > biggest[0]:
                biggest = [nums[j], j]
            if nums[j] < smallest[0]:
                smallest = [nums[j], j]
        if biggest == smallest: break
        nums[biggest[1]] = math.ceil(nums[biggest[1]] / smallest[0])
        result.append((biggest[1]+1, smallest[1]+1))
    print(len(result))
    for a, b in result:
        print(a, b)

