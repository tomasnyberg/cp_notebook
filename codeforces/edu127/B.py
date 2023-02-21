import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def test(add_to_first, nums):
    nums[0] += add_to_first
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            nums[i] +=1
        elif nums[i] - nums[i-1] > 1:
            nums[i] -= 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            return False
    return True

            

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    if any(test(i, [x for x in nums]) for i in [-1,0,1]):
        print("YES")
    else:
        print("NO")