import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from queue import deque

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
    dq = deque()
    for x in nums:
        if not dq or x < dq[0]:
            dq.appendleft(x)
        else:
            dq.append(x)
    nums = list(dq)
    print(nums)
    result = [0]
    merge_sort(nums, result)
    print(result[0])
