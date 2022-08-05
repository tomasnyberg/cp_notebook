import sys

lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines),2):
    n, k = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort()
    counts = {}
    prev = -1
    greaterequaltok = 0
    smallest = nums[0]
    best = (-1, [-1, -1])
    for x in nums:
        if prev != x - 1 and prev != x or (prev != x and greaterequaltok != len(counts)):
            counts.clear()
            greaterequaltok = 0
            smallest = x
        prev = x
        counts[x] = 1 if x not in counts else counts[x] + 1
        if counts[x] == k: greaterequaltok+=1
        if greaterequaltok == len(counts) and x - smallest > best[0]:
            # print("found new good")
            best = (x-smallest, [smallest, x])
    if best[0] == -1:
        print(-1)
    else:
        print(best[1][0], best[1][1])
    # print()
        