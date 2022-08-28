import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n, p, k = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1]))
    x, y = map(int, lines[i+2].split(" "))
    need_to_fill = {j:0 for j in range(k)}
    for j in range(p-1, len(nums)):
        if not nums[j]:
            need_to_fill[(j-(p-1))%k]+=1
    best = 10**9
    for j in range(p-1, n):
        offset = (j-(p-1))%k
        best = min(best, (j-(p-1))*y + need_to_fill[offset]*x)
        need_to_fill[offset] -= 1 if not nums[j] else 0
    print(best)