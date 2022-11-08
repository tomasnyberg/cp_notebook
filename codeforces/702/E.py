import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

def check(numscopy, idx, CS):
    curr = CS[idx]
    for i in range(idx+1, len(numscopy)):
        if curr < numscopy[i]:
            return False
        curr += numscopy[i]
    return True

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    numscopy = nums.copy()
    numscopy.sort()
    CS = cum_sum(numscopy)
    low = 0
    high = len(nums)
    while low < high:
        mid = (low + high) >> 1
        if check(numscopy, mid, CS):
            high = mid
        else:
            low = mid + 1
    needed_at_least = numscopy[low]
    result = []
    for idx, x in enumerate(nums):
        if x >= needed_at_least:
            result.append(idx+1)
    print(len(result))
    print(*result)
            
