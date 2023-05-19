import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    parents = [i for i in range(len(nums))]
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)
    for i in range(len(nums)):
        union(i, nums[i]-1)
    highest = (len(set(find(i) for i in range(len(nums)))))
    seen = set()
    incycle = [0]
    def dfs(x):
        start = x
        iterations = 0
        while x not in seen or x == start:
            # print(x)
            if x == start and iterations > 2:
                incycle[0] += iterations
                return 1
            iterations += 1
            seen.add(x)
            x = nums[x] - 1
        # print()
        return 0
    lowest = 0
    for i in range(len(nums)):
        lowest += dfs(i)
    if incycle[0] == len(nums): lowest -= 1
    print(lowest + 1, highest)
    