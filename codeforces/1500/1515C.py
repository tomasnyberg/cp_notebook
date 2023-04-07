import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappop, heappush

for i in range(1, len(lines), 2):
    n, m, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    for j in range(len(nums)):
        nums[j] = [nums[j], j]
    nums.sort(key=lambda x: x[0])
    towers = [(0, j) for j in range(m)]
    taken = {}
    while nums:
        height, index = heappop(towers)
        block, pos = nums.pop()
        taken[pos] = index
        newtower = (height + block, index)
        heappush(towers, newtower)
    # for height, index in towers:
    #     print("tower", index,"has height", height)
    smallest = min([height for height, index in towers])
    biggest = max([height for height, index in towers])
    if biggest-smallest > x:
        print(-1)
        continue
    resultarr = [(index, taken[index]) for index in taken]
    resultarr.sort()
    print("YES")
    for _, tower in resultarr:
        print(tower + 1, end=" ") 
    print()
