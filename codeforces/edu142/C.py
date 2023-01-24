import sys
from bisect import bisect_left
lines = list(map(str.strip, sys.stdin.readlines()))

def pair(a, n):
    return a, n - a + 1

def check(mid, n, nums):
    nums = nums.copy()
    removed = set()
    while mid >= 1:
        a, b = pair(mid, n)
        removed.add(a)
        removed.add(b)
        mid -= 1
    xs = []
    for x in nums:
        if x not in removed:
            if not xs or x > xs[-1]:
                xs.append(x)
            else:
                return False
    return True

# print(check(1, 5, [1,5,4,3,2]))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    low = 0
    high = len(nums)//2
    while low < high:
        mid = (low + high)//2
        if check(mid, len(nums), nums):
            high = mid
        else:
            low = mid + 1
    print(low)