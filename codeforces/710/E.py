import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    taken = set([nums[0]])
    result = [nums[0]] + [0]*(len(nums)-1)
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            result[i] = nums[i]
            taken.add(nums[i])
    maximal = result.copy()
    minimal = result.copy()
    ptr = 1
    for i in range(len(minimal)):
        while ptr in taken: ptr+=1
        if result[i]: continue
        minimal[i] = ptr
        ptr += 1
    taken = set(maximal)
    available = [i for i in range(1, nums[0]) if i not in taken]
    biggestseen = nums[0]
    for i in range(len(minimal)):
        if maximal[i] > biggestseen:
            for j in range(biggestseen+1, maximal[i]+1):
                if j not in taken:
                    available.append(j)
            biggestseen = maximal[i]
        if maximal[i]: continue
        maximal[i] = available.pop()
    print(*minimal)
    print(*maximal)
