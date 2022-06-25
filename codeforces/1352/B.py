import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_res(nums):
    print("YES")
    for x in nums:
        print(x, end=" ")
    print()

for line in lines[1:]:
    n, k = map(int, line.split(" "))
    if k > n:
        print("NO")
        continue
    num = n // k
    sum_rn = num * k
    want = n - sum_rn
    nums = [num]*k
    if (num + want) % 2 == num % 2:
        nums[0] += want
        print_res(nums)
        continue
    nums = list(map(lambda x: x-1, nums)) # Change parity
    sum_rn -= k
    want = n - sum_rn
    num = nums[0]
    if num == 0:
        print("NO")
        continue
    if (num + want) % 2 == num % 2:
        nums[0] += want
        print_res(nums)
        continue
    print("NO")


