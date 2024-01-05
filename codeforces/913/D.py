import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

def solve(intervals, k):
    x = 0
    furthestl = 0
    furthestr = 0
    for l, r in intervals:
        if l <= x <= r:
            furthestl = max(l, furthestl - k)
            furthestr = min(r, furthestr + k)
        elif x < l:
            if furthestr + k < l:
                return False
            furthestl = l
            furthestr = min(r, furthestr + k)
        else:
            if furthestl - k > r:
                return False
            furthestl = max(l, furthestl - k)
            furthestr = r
        x = (furthestl + furthestr) // 2
    return True

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    intervals = []
    ii+=1
    for _ in range(n):
        intervals.append(list(map(int, lines[ii].split())))
        ii += 1
    low = 0
    high = 10**12
    while low < high:
        mid = (low + high) // 2
        if solve(intervals, mid):
            high = mid
        else:
            low = mid + 1
    print(low)