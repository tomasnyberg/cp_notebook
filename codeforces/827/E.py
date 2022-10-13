import sys, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

def binary_search(nums, target):
    low = 0
    high = len(nums)
    while low < high:
        mid = (low + high) >> 1
        if nums[mid] > target:
            high = mid 
        else:
            low = mid + 1
    return low

for i in range(1, len(lines), 3):
    n, q = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    queries = list(map(int, lines[i+2].split(" ")))
    biggests_so_far = []
    biggest = 0
    for x in nums:
        biggest = max(biggest, x)
        biggests_so_far.append(biggest)
    CS = cum_sum(nums)
    # print(biggests_so_far)
    # print(CS)
    for q in queries:
        idx = binary_search(biggests_so_far, q)
        # print(idx, q)
        if idx == len(nums):
            print(CS[-1], end=" ")
        elif idx == 0:
            if q >= biggests_so_far[0]:
                print(CS[0], end=" ")
            else:
                print(0, end=" ")
        else:
            print(CS[idx] if q >= biggests_so_far[idx] else CS[idx - 1], end=" ")
    print()
    