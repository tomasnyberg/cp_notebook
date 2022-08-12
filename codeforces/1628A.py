import sys
import bisect
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    occurrences = {}
    for idx, x in enumerate(nums):
        if x in occurrences:
            occurrences[x].append(idx)
        else:
            occurrences[x] = [idx]
    kpos = 0
    ans = []
    # print(occurrences)
    while kpos < len(nums):
        # print(kpos)
        furthesttaken = kpos
        for i in range(len(nums)+1):
            if i not in occurrences or kpos > occurrences[i][-1]:
                if kpos == furthesttaken: furthesttaken +=1
                ans.append(i)
                break
            takeindex = occurrences[i][bisect.bisect_left(occurrences[i], kpos)]
            furthesttaken = max(furthesttaken, takeindex+1)
            # print("Take", i, "at index", takeindex, "furthesttaken", furthesttaken)
        kpos = furthesttaken
    print(len(ans))
    for x in ans:
        print(x, end=" ")
    print()