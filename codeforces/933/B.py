import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    ops = nums[0]
    for i in range(1, len(nums)-1):
        if nums[i] // 2 < ops:
            print("NO")
            break
        nums[i-1] -= ops
        nums[i] -= 2 * ops
        nums[i+1] -= ops
        ops = nums[i]
    else:
        print("YES" if all(x == 0 for x in nums) else "NO")
    # print(nums)
    # print(ops)