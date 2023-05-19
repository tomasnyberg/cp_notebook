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