import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(x, target, nums):
    parity = x % 2 # 0 or 1 obviously
    for num in nums:
        par = num % 2
        sum = parity + par
        if sum == 0 or sum == 2:
            parity = 0
        else:
            parity = 1
    return target % 2 == parity

for i in range(1, len(lines), 2):
    n, x, target = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    binnums = list(map(lambda x: bin(x)[2:], nums))
    if solve(x, target, nums):
        print("Alice")
    else:
        print("Bob")