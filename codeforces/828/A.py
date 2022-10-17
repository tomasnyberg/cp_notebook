import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    nums = list(map(int, lines[i+1].split(" ")))
    a = lines[i+2]
    if len(nums) != len(a):
        print("NO")
        continue
    seen = {}
    bad = False
    for j in range(len(nums)):
        if nums[j] in seen:
            if seen[nums[j]] != a[j]:
                # print("bad at", j, seen)
                bad = True
                break
        else:
            seen[nums[j]] = a[j]
    print("NO" if bad else "YES")