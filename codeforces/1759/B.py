import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    m, s = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    seen = set(nums)
    if len(seen) != len(nums):
        print("NO")
        continue
    gotten = 0
    for j in range(1, max(nums)):
        if j not in seen:
            gotten += j
    for j in range(max(seen) + 1, 1000):
        if gotten >= s: break
        gotten += j
    print("YES" if gotten == s else "NO")