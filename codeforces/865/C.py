import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(xs):
    if len(xs) == 2:
        return xs[0] <= xs[1]
    for i in range(1, len(xs)-1):
        if xs[i-1] > xs[i] < xs[i+1]:
            return False
    return True

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if len(nums) % 2 == 1:
        a = check(nums[:-1])
        b = check(nums[1:])
        print("YES" if a or b else "NO")
    else:
        print("YES" if check(nums) else "NO")
    