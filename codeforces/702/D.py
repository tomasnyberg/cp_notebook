import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def recur(xs, result, depth):
    if not xs: return
    biggest = [-1, -1]
    for idx, x in enumerate(xs):
        if x > biggest[0]:
            biggest = [x, idx]
    result[biggest[0]] = depth
    recur(xs[:biggest[1]], result, depth+1)
    recur(xs[biggest[1]+1:], result, depth+1)


for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    result = {}
    recur(nums, result, 0)
    for i in nums:
        print(result[i], end=" ")
    print()