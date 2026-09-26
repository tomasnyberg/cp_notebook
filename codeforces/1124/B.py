import sys
from collections import defaultdict
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

# A -> B -> C -> D -> C 2
# E -> C -> D -> C]-> D <- before: 1%2 == 1 so: D
# C -> D -> C]-> D -> C <- before: 0%2==0, so: C
# F -> D -> C -> D]-> C <- gets in at D, but with 1%2 = 1 before. So 


# So we enter the cycle, but after how many turns?
# find the starting point in the cycle
# and how many 
# find the SAME cycles
# only q really is is their entry point the same?

seen = {}
def next(num):
    if num in seen:
        return seen[num]
    result = 0
    while num > 0:
        result += (num%10)**2
        num//=10
    seen[num] = result
    return result

def equilibrium(num):
    seen = { num: 1 }
    curr = [num]
    while next(curr[-1]) != curr[-1]:
        curr.append(next(curr[-1]))
        if curr[-1] in seen:
            cycle_len = len(curr) - seen[curr[-1]]
            before = len(curr) % cycle_len
            # print(curr, cycle_len, before)
            actual = curr[-1 - before]
            return actual
        #TODO: we gotta find the entry point in the cycle
        seen[curr[-1]] = len(curr)
    return curr[-1]

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    eq_counts = defaultdict(int)
    result = 0
    for x in nums:
        eq = equilibrium(x)
        result += eq_counts[eq]
        eq_counts[eq] += 1
    print(result)

