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
        
# print(check_good([1,-1,2,-2,3,-3]))
        

# import random
# seen = set()
# for i in range(10000000):
#     xs = [random.randint(-4,4) for i in range(4)]
#     if tuple(xs) in seen: continue
#     if check_good(xs):
#         seen.add(tuple(xs))
#         print(xs)

good_len_4 = [[-1, -1, -1, 2],
[2, -1, -1, -1],
[-1, 2, -1, -1],
[-1, -1, 2, -1],
[2, 2, 2, 2],
[0, 0, 0, 0]]

# print(good_len_4)

def prefix_product(nums):
    p = 1
    result = []
    for n in nums:
        p *= n
        result.append(p)
    return result

def prefix_sum(nums):
    s = 0
    result = []
    for n in nums:
        s += n
        result.append(s)
    return result

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    if len(nums) == 2:
        print(max(nums) - min(nums))
        continue
    if len(nums) == 4:
        nums.sort()
        res = 10**9
        for xs in good_len_4:
            xs.sort()
            res = min(res, (sum(abs(a-b) for a,b in zip(nums, xs))))
        print(res)
        continue
    else:
        # Print the sum of the absolute values of x
        total = 0
        for x in nums:
            total += abs(x)
        print(total - 3)
        
