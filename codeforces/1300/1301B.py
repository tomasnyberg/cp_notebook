import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if all(x == -1 for x in nums):
        print(0, 0)
        continue
    smallest = min(x for x in nums if x != -1)
    low = 0
    high = 10**10
    def test(x):
        xs = nums[:]
        max_diff = 0
        for i in range(len(xs)):
            if xs[i] == -1:
                xs[i] = smallest + x
            if i-1 >= 0:
                max_diff = max(max_diff, abs(xs[i]-xs[i-1]))
        return max_diff <= x
    while low < high:
        mid = (low+high)//2
        if test(mid):
            high = mid
        else:
            low = mid+1
    print(low, smallest + low)
    
        