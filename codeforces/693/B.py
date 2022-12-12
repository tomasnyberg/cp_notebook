import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    a, b = 0, 0
    for x in nums:
        if x == 1:
            a += 1
        else:
            b += 1
    total = a + 2*b
    if total % 2 != 0:
        print("NO")
        continue
    nums.sort()
    alice = 0
    bob = 0
    while nums:
        if alice <= bob:
            alice += nums.pop()
        else:
            bob += nums.pop()
    print("YES" if alice == bob else "NO")