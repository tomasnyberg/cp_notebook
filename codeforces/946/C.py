import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    counts_all = {}  # (a,b,_) i.e. all counts of things that start with this
    counts_exact = {}  # (a,b,c) i.e. all counts of things that start with this
    result = 0
    for i in range(len(nums)-2):
        triple = (nums[i], nums[i+1], nums[i+2])
        if triple not in counts_exact:
            counts_exact[triple] = 0
        for j in range(3):
            temp = list(triple)
            temp[j] = -1
            temp = tuple(temp)
            if temp not in counts_all:
                counts_all[temp] = 0
            result += counts_all[temp]
            counts_all[temp] += 1
            result -= counts_exact[triple]
        counts_exact[triple] += 1
    print(result)
