import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    running = 0
    for x in nums:
        running ^= x
    if running == 0:
        print("YES")
        continue
    good = True
    count = 0
    while nums:
        curr = nums.pop()
        while nums and curr != running or (nums and nums[-1] == 0):
            curr ^= nums.pop()
        if curr != running:
            good = False
            break
        count += 1
    print("YES" if good and count >= 2 else "NO")

