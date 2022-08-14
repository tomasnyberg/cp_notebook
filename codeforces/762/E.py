import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    sum = 0
    counts = {}
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
    stack = []
    bad = False
    for i in range(0, len(nums)+1):
        if bad:
            print(-1, end=" ")
            continue
        if i > 0 and i-1 not in counts:
            if not stack:
                bad = True
                print(-1, end= " ")
                continue
            biggest = stack.pop()
            sum += i - 1 - biggest
        print(sum + (counts[i] if i in counts else 0), end=" ")
        while i > 0 and i - 1 in counts and counts[i-1] > 1:
            stack.append(i-1)
            counts[i-1] -= 1
    print()
    