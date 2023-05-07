import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    tuples = {}
    result = 0
    for i, x in enumerate(nums):
        tuples[i + 1] = x
    for i, x in enumerate(nums):
        original = x
        idx = i+1
        while x <= len(nums) * 2:
            diff = x - idx
            if diff <= 0:
                x += original
                continue
            if diff >= idx: break
            if tuples[diff] == x // original:
                # print("Found pair", diff, idx)
                result += 1
            x += original
    print(result)

                

        
