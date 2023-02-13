import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def find_next(a_nums, b_nums, start):
    res = [10**9, 10**9, 10**9]
    for j in range(start, len(a_nums)):
        cand = [a_nums[j], b_nums[j], j]
        if cand < res:
            res = cand
    return res

for i in range(1, len(lines), 3):
    a_nums = list(map(int, lines[i+1].split()))
    b_nums = list(map(int, lines[i+2].split()))
    swaps = []
    start = 0
    while start < len(a_nums):
        _, _, j = find_next(a_nums, b_nums, start)
        a_nums[start], a_nums[j] = a_nums[j], a_nums[start]
        b_nums[start], b_nums[j] = b_nums[j], b_nums[start]
        if start != j:
            swaps.append([start+1, j+1])
        start += 1
    if a_nums == sorted(a_nums) and b_nums == sorted(b_nums):
        print(len(swaps))
        for swap in swaps:
            print(*swap)
    else:
        print(-1)    

    