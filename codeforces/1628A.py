import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    kpos = 0
    # print(nums)
    candidates = []
    while kpos < len(nums):
        candidate = [-1, -1] # How big this k should be, the max
        seen = set()
        maxseen = -1
        for i in range(kpos, len(nums)):
            maxseen = max(nums[i], maxseen)
            seen.add(nums[i])
            if len(seen) == maxseen + 1 and candidate[-1] != maxseen:
                candidate = [i-kpos+1, maxseen]
        # print(candidate)
        if candidate[0] == -1:
            if 0 in seen:
                candidates.append([-1, 0])
            else:
                candidates.append([-1, -1])
            break
        candidates.append(candidate)
        kpos += candidate[0]
    print(len(candidates))
    for seen, big in candidates:
        if big == -1:
            print(0, end=" ")
        else:
            print(big + 1, end= " ")
    print()