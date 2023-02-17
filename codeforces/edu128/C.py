import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import bisect

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for line in lines[1:]:
    line = list(line)
    while line and line[-1] == '0':
        line.pop()
    line = line[::-1]
    while line and line[-1] == '0':
        line.pop()
    line = line[::-1]
    if not line:
        print(0)
        continue
    line = [1 if x == '1' else 0 for x in line]
    inverted = [1 if x == 0 else 0 for x in line]
    zero_cs = cum_sum(inverted)
    total = sum(line)
    CS_LEFT = cum_sum(line)
    CS_RIGHT = cum_sum(line[::-1])
    # print(line)
    indices_left = {}
    indices_right = {}
    for i in range(1, total + 1):
        # find last index such that it equals i in CS_left
        idx = bisect.bisect_right(CS_LEFT, i) - 1
        indices_left[i] = idx
        idx = len(CS_RIGHT) - bisect.bisect_right(CS_RIGHT, i)
        indices_right[i] = idx
    CS_RIGHT = CS_RIGHT[::-1]
    # print(indices_left)
    # print(indices_right)
    # Can we end up with maximum x removed and maximum x 0s remaining?
    def check(x):
        for i in range(x+1):
            left = indices_left[i] + 1 if i in indices_left else 0
            right = indices_right[x-i] - 1 if x-i in indices_right else len(line) - 1
            # How many zeroes are there between left and right?
            zeroes = zero_cs[right] - zero_cs[left-1] if left > 0 else zero_cs[right]
            # print(i, x-i, left, right)
            if zeroes <= x:
                return True
        return False
            # Remove i from the left, and x - i from the right
    low = 0
    high = total
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    print(low)
