import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    extra = k % 2
    attacks = k // 2
    for _ in range(2):
        for i in range(n):
            if attacks > nums[i]:
                attacks -= nums[i]
                nums[i] = 0
            else:
                nums[i] -= attacks
                break
        attacks = k // 2
        nums.reverse()
    if extra:
        for i in range(n):
            if nums[i] > 0:
                nums[i] -= 1
                break
    print(nums.count(0))

