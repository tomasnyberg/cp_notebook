import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    running = 1
    if nums[0] != 1:
        print("NO")
        continue
    for x in nums[1:]:
        if x > running:
            print("NO")
            break
        running += x
    else:
        print("YES")

        