import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def area(height, width):
    return (height * width) / 2

for ii in range(1, len(lines), 2):
    n, d, h = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    result = 0
    for x in nums:
        result += area(h, d)
    proportion = d / h
    for i in range(len(nums) - 1):
        overlap = nums[i] + h - nums[i+1]
        # print("overlap between triangle at", nums[i], "and", nums[i+1], "is", overlap)
        if overlap > 0:
            result -= area(overlap, d - (h-overlap)*proportion)
    print(result)