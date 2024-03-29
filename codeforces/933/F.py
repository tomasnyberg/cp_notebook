import sys
from bisect import bisect_left
lines = list(map(str.strip, sys.stdin.readlines()))
# lines = open('./codeforces/933/in').read().strip().split('\n')
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 4):
    n, m, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii + 1].split()))
    b = list(map(int, lines[ii + 2].split()))
    c = list(map(int, lines[ii + 3].split()))
    maxd = [0,-1]
    for i in range(1, len(a)):
        if a[i] - a[i-1] > maxd[0]:
            maxd = [a[i] - a[i-1], i]
    b = sorted(set(b))
    c = list(sorted(set(c)))
    low = 0
    high = maxd[0]
    lb = a[maxd[1] - 1]
    rb = a[maxd[1]]
    in_c = set(c)
    def check(mid):
        for x in b:
            first_bound = lb + mid
            second_bound = rb - mid
            left = min(first_bound, second_bound)
            right = max(first_bound, second_bound)
            left_middle = left + (right - left) // 2
            right_middle = left_middle + 1 if right != left else left_middle
            for middle in [left_middle, right_middle]:
                target = middle - x
                idx = bisect_left(c, target)
                if idx < len(c) and x + c[idx] <= first_bound and x + c[idx] >= second_bound:
                    return True
            # idx = bisect_right(c, target)
            # if idx > 0 and c[idx-1] == target:
            #     return True
            # if (idx < len(c) and c[idx] + x <= right):
            #     return True
        return False
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    # print(a)
    a.append(a[maxd[1]-1] + low)
    a.sort()
    # print(a)
    maxd = 0
    for i in range(1, len(a)):
        maxd = max(maxd, a[i] - a[i-1])
    print(maxd)