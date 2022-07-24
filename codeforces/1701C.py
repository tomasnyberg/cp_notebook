import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    workers, tasks = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    proficientcounts = [0]*workers
    for x in nums:
        proficientcounts[x-1]+=1
    low = 0
    high = 2*len(nums)
    while low <= high:
        t = (high + low) >> 1
        extras = 0
        uncompleted = 0 
        for w in range(workers):
            can_complete = min(t, proficientcounts[w])
            extras += (t- can_complete) >> 1
            uncompleted += proficientcounts[w] - can_complete 
        if uncompleted <= extras:
            high = t - 1
        else:
            low = t + 1
    print(low)