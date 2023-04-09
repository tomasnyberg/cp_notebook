import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(xs):
    if len(xs) == 2:
        return xs[0] <= xs[1]
    count = 0
    for i in range(1, len(xs)):
        if (xs[i-1] if i-1 >= 0 else 10**15) > xs[i] < (xs[i+1] if i+1 < len(xs) else 10**15):
            count += 1
    return count <= 1

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    print(nums)
    for i in range(1, len(nums)):
        if i != 1 and nums[i-2] > nums[i-1]:
            to_add = nums[i-2] - nums[i-1]
            nums[i-1] += to_add
            nums[i] += to_add 
        if i != len(nums)-1 and nums[i+1] < nums[i]:
            to_add = nums[i+1] + nums[i]
            nums[i-1] += to_add
            nums[i] += to_add 
    print(nums)
    if len(nums) % 2 == 1:
        a = nums[1:] == list(sorted(nums[1:]))
        b = nums[:-1] == list(sorted(nums[:-1]))
        print("YES" if a or b else "NO")
    else:
        print("YES" if nums == list(sorted(nums)) else "NO")
    