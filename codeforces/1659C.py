import sys
lines = list(map(str.strip, sys.stdin.readlines()))
for i in range(1, len(lines), 2):
    n, a, b = map(int, lines[i].split(" "))
    nums = [0] + list(map(int, lines[i+1].split(" ")))
    smallest = float("inf")
    for f in range(0, n+1):
        curr = a*nums[f]+b*(sum(nums) - sum(nums[:f+1]) - (n-f-1)*nums[f])
        smallest = min(curr, smallest)
    print(smallest)