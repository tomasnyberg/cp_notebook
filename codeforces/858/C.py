import sys
import itertools
lines = list(map(str.strip, sys.stdin.readlines()))

def check_good(xs):
    m = len(xs) // 2
    # Get every subsequence of length m, and all the elements that are not in that subsequence in two different arrays
    combos = [1]*m + [0]*m
    for combo in itertools.permutations(combos, 2*m):
        a = [x for x, c in zip(xs, combo) if c == 1]
        b = [x for x, c in zip(xs, combo) if c == 0]
        prod = 1
        for x in a:
            prod *= x
        if prod != sum(b):
            return False
    return True

def distance(a, b):
    total = 0
    for x, y in zip(a, b):
        total += abs(x-y)
    return total

# print(check_good([-1,-1,-1,-1,-1,-1,-1,4]))

good_len_4 = [[-1, -1, -1, 2],
[2, 2, 2, 2],
[0, 0, 0, 0]]

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    n = len(nums) // 2
    nums.sort()
    if len(nums) == 2:
        print(max(nums) - min(nums))
        continue
    if len(nums) == 4:
        res = 10**25
        for good in good_len_4:
            good.sort()
            res = min(res, sum(abs(x-y) for x,y in zip(nums, good)))
        print(res)
        continue
    if n % 2 == 0:
        candidates = [[-1]*(2*n - 1) + [n], [0] * (2*n)]
        res = 10**25
        for c in candidates:
            res = min(res, sum(abs(x-y) for x,y in zip(nums, c)))
        print(res)
    else:
        print(sum(abs(x-y) for x,y in zip(nums, [0]*(2*n))))
        

        
