import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for i in range(1, len(lines), 2):
    n, c, d = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort(key=lambda x: -x)
    CS = cum_sum(nums)
    if CS[d-1 if d-1 < len(CS) else -1] >= c:
        print("Infinity")
        continue
    if nums[0] * d < c:
        print("Impossible")
        continue
    print(0)
    