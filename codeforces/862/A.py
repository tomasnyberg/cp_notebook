import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(xs, x):
    bs = []
    for a in xs:
        bs.append(a ^ x)
    res = 0
    for b in bs:
        res ^= b
    return res == 0

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    for i in range(2**8):
        if check(nums, i):
            print(i)
            break
    else:
        print(-1)
        