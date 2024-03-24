import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import math
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    xs = list(map(int, line))
    rights_remaining = sum(xs)
    lefts_remaining = len(xs) - rights_remaining
    lefts = 0
    rights = 0
    result = (10**9, -1)
    if rights_remaining >= int(math.ceil(len(xs) / 2)):
        result = min(result, (len(xs)//2, 0))
    for i, x in enumerate(xs):
        lefts += 1 if x == 0 else 0
        rights += 1 if x == 1 else 0
        lefts_remaining -= 1 if x == 0 else 0
        rights_remaining -= 1 if x == 1 else 0
        left_citizens = i+1
        right_citizens = len(xs) - i - 1
        if int(math.ceil(left_citizens/2)) <= lefts and int(math.ceil(right_citizens/2)) <= rights_remaining:
            # print(i, "is a valid pos with score")
            result = min(result, (abs(len(xs)/2 - (i + 1)), i+1))
    print(result[1])
            

