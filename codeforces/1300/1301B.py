import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if all(x == -1 for x in nums):
        print(0, 0)
        continue
    smallest = [-1,-1] # [value, index]
    for i in range(len(nums)):
        if nums[i] != -1 and ((i-1 >= 0 and nums[i-1] == -1) or (i+1 < len(nums) and nums[i+1] == -1)):
            if smallest[0] == -1 or nums[i] < smallest[0]:
                smallest = [nums[i], i]
    # print(smallest)
    low = 0
    high = 10**10
    # Can we get a diff that is at most x?
    def test(x):
        xs = nums[:]
        max_diff = 0
        for i in range(len(xs)):
            if xs[i] == -1:
                xs[i] = smallest[0] + x
            if i-1 >= 0:
                max_diff = max(max_diff, abs(xs[i]-xs[i-1]))
        return max_diff <= x
    while low < high:
        mid = (low+high)//2
        if test(mid):
            high = mid
        else:
            low = mid+1
    print(low, smallest[0] + low)
    
        