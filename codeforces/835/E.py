import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def merge_sort(xs, result):
    def merge(left, right, result):
        a = 0
        b = 0
        merged = []
        while a < len(left) or b < len(right):
            if a == len(left) or b == len(right):
                merged += left[a:]
                merged += right[b:]
                break
            # Note, you can change this to < if you don't want to count an equal element as an inversion
            if left[a] <= right[b]:
                merged.append(left[a])  
                a += 1
            else:
                merged.append(right[b])
                b += 1
                result[0] += len(left) - a
        return merged
    if len(xs) == 1:
        return xs
    n = len(xs)
    return merge(merge_sort(xs[:n//2], result), merge_sort(xs[n//2:], result), result)

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    othernums = nums.copy()
    thirdnums = nums.copy()
    for idx, x in enumerate(nums):
        if x == 0:
            othernums[idx] = 1
            break
    for i in range(len(nums)- 1,-1,-1):
        if nums[i] == 1:
            thirdnums[i] = 0
            break
    result1 = [0]
    result2 = [0]
    result3 = [0]

    merge_sort(nums, result1)
    merge_sort(othernums, result2)
    merge_sort(thirdnums, result3)
    print(max(result1[0], result2[0], result3[0]))
