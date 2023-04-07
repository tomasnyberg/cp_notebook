import sys

lines = list(map(str.strip, sys.stdin.readlines()))
i = 1
def select_best_possible(remaining_moves, nums):
    to_reduce = nums[0]
    for num in nums:
        if num - remaining_moves > 97:
            return num
        to_reduce = max(to_reduce, num)
    return to_reduce

while i < len(lines):
    n, k = map(int, lines[i].split(" "))
    str = lines[i+1]
    nums = list(map(ord, str))
    for j in range(min(26, k)):
        remaining_moves = min(26,k) - j - 1
        to_reduce = select_best_possible(remaining_moves, nums)
        if to_reduce == 97:
            break
        for idx, num in enumerate(nums):
            if num == to_reduce:
                nums[idx] -= 1
    print(''.join(list(map(chr, nums))))
    i += 2

