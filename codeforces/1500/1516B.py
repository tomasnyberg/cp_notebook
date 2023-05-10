import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    n = len(nums)
    prefix = [0] * 2005
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] ^ nums[i - 1]
    good = False
    for i in range(1, n+1):
        if prefix[i] == prefix[n]^prefix[i]:
            good = True
    for i in range(1, n+1):
        for j in range(i+1, n):
            good |= prefix[i] == (prefix[j]^prefix[i]) == (prefix[n]^prefix[j])
    print("YES" if good else "NO")
        

