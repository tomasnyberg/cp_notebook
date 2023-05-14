import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def beauty(xs):
    right = list(sorted(xs))
    while xs and xs[-1] == right[-1]:
        xs.pop()
        right.pop()
    xs.reverse()
    right.reverse()
    while xs and xs[-1] == right[-1]:
        xs.pop()
        right.pop()
    return len(xs) - 1 if xs else 0


for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    # Generate every single subarray of nums
    result = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            result += beauty(nums[i:j+1])
    print(result)