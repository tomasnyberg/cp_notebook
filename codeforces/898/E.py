import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, x = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    low = 0
    high = 10**15
    def check(mid):
        total = 0
        for num in nums:
            total += max(0, mid - num)
        return total > x
    while low < high:
        mid = (low+high)//2
        if check(mid):
            high = mid
        else:
            low = mid+1
    print(low - 1)