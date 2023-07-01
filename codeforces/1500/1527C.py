import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import Counter


for line in lines[2::2]:
    nums = list(map(int, line.split()))
    to_add = {} # number -> sum of the amount of elements to the left
    result = 0
    for i, x in enumerate(nums):
        to_right = len(nums) - i
        if x in to_add:
            result += to_add[x] * to_right
            to_add[x] += i + 1
        else:
            to_add[x] = i + 1
    print(result)
            
