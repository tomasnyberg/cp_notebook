import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(x, target, nums):
    parity = x % 2
    for num in nums:
        parity = (num%2)^parity
    return target % 2 == parity

for i in range(1, len(lines), 2):
    n, x, target = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    print("Alice" if solve(x, target, nums) else "Bob")
