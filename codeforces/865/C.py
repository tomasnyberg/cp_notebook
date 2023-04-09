import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(xs):
    if len(xs) == 2:
        return xs[0] <= xs[1]
    count = 0
    for i in range(len(xs)):
        if (xs[i-1] if i-1 >= 0 else 10**15) > xs[i] < (xs[i+1] if i+1 < len(xs) else 10**15):
            count += 1
    return count <= 1

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if len(nums) % 2 == 1:
        a = check(nums[:-1])
        b = check(nums[1:])
        print("YES" if a or b else "NO")
    else:
        print("YES" if check(nums) else "NO")
    