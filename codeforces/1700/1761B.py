import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check_delete(xs):
    for i in range(1, len(xs)):
        if xs[i] == xs[i-1]:
            del xs[i]
            return True
    if xs[-1] == xs[0] and len(xs) > 1:
        xs.pop()
        return True
    return False

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    while check_delete(nums):
        continue
    s = set(nums)
    if len(s) == 2:
        print(len(nums) // 2 + 1)
        continue
    else:
        print(len(nums))
                