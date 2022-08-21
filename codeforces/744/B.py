from cgitb import small
import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappush, heappop
from collections import deque

# Rotate an array from a starting index to an ending index to the left by k steps
def rotate(arr, start, end, k):
    if k == 0: return
    k %= end - start + 1
    while k > 0:
        temp = arr[start]
        for i in range(start, end):
            arr[i] = arr[i+1]
        arr[end] = temp
        k -= 1


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
            rotate(nums, i, smallest[1], rotationsneeded)
            rotations.append([i+1, smallest[1] + 1, rotationsneeded])
    print(len(rotations))
    for start, end, amount in rotations:
        print(start, end, amount)


