import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def find_smallest(nums):
    prev = 0
    result = nums[-1]
    for x in nums:
        result = min(x - prev - 1, result)
        prev = x
    return result

def find_candidates(nums, smallest):
    prev = 0
    for x in nums:
        if x - prev - 1 == smallest:
            if prev == 0:
                return [x]
            else:
                return [prev, x]
        prev = x

def point_in_biggest_gap(nums):
    biggest_gap = [0, -1, -1]
    prev = 0
    for x in nums:
        gap = x - prev
        if gap > biggest_gap[0]:
            biggest_gap = [gap, prev, x]
        prev = x
    return (biggest_gap[2] - biggest_gap[1])//2 + biggest_gap[1]

def insert_in_list(nums, point):
    result = nums.copy()
    i = 0
    while i < len(nums) and nums[i] < point:
        i += 1
    if i == len(nums):
        result.append(point)
        return result
    else:
        result.insert(i, point)
        return result

for i in range(2, len(lines), 3):
    n, d = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    smallest = find_smallest(nums)
    candidates = find_candidates(nums, smallest)
    best = smallest
    for candidate in candidates:
        nums_without_c = list(filter(lambda x: x != candidate, nums))
        point_candidates = [point_in_biggest_gap(nums_without_c)] + [d]
        for pc in point_candidates:
            new_list = insert_in_list(nums_without_c, pc)
            best = max(find_smallest(new_list), best)
    print(best)