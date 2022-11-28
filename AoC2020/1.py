import sys
lines = list(map(str.strip, sys.stdin.readlines()))

nums = []
for line in lines:
    nums.append(int(line))

def part_one():
    seen = set()
    for x in nums:
        target = 2020 - x
        if target in seen:
            return (target * x)
        seen.add(x)

def part_two():
    nums.sort()
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums) - 1
        while left < right:
            target = 2020 - nums[i] - nums[left] - nums[right]
            if target == 0:
                return (nums[i] * nums[left] * nums[right])
            elif target < 0:
                right -= 1
            else:
                left += 1

print("Part one answer:", part_one())
print("Part two answer:", part_two())
