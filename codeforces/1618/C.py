import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    evengcd = nums[0]
    oddgcd = nums[1]
    for i in range(len(nums)):
        if i % 2 == 0:
            evengcd = gcd(evengcd, nums[i])
        else:
            oddgcd = gcd(oddgcd, nums[i])
    if evengcd == oddgcd:
        print(0)
    else:
        found = False
        for idx, x in enumerate([evengcd, oddgcd]):
            div = evengcd if idx == 0 else oddgcd
            bad = False
            for i in range(1 if idx == 0 else 0, len(nums), 2):
                if nums[i] % div == 0:
                    bad = True
                    break
            if not bad:
                found = True
                print(x)
                break
        if not found: print(0)
