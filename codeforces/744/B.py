from cgitb import small
import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappush, heappop
from collections import deque

# Left shift all elements in array starting from start and ending at end by k steps
def rotate(arr, start, end, k):
    result = arr.copy()
    len = end-start+1
    k %= len
    for i in range(start, end+1):
        result[(i-start-k)%len+start] = arr[i]
    return result


for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    rotations = []
    for i in range(len(nums)):
        smallest = [nums[i], i]
        for j in range(i, len(nums)):
            if nums[j] <= smallest[0]:
                smallest = [nums[j], j]
        if smallest[1] != i:
            rotationsneeded = smallest[1] - i
            nums = rotate(nums, i, smallest[1], rotationsneeded)
            rotations.append([i+1, smallest[1] + 1, rotationsneeded])
    print(len(rotations))
    # print(nums)
    for start, end, amount in rotations:
        print(start, end, amount)


