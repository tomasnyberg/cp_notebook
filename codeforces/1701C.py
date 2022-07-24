import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    workers, tasks = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    proficientcounts = [0]*workers
    for x in nums:
        proficientcounts[x-1]+=1
    low = 0
    high = len(nums)*2
    while low <= high:
        t = (high + low) >> 1
        twohour_ones = 0
        notcompleted = 0
        for w in range(workers):
            completed = min(t, proficientcounts[w]) # How many tasks this worker completed
            twohour_ones += (t - completed) >> 1
            notcompleted += proficientcounts[w] - completed 
        if notcompleted <= twohour_ones:
            high = t-1
        else:
            low = t+1
    print(low)