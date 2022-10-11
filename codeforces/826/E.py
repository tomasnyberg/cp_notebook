import sys
lines = list(map(str.strip, sys.stdin.readlines()))
sys.setrecursionlimit(200002)

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    # print(nums)
    edges = []
    for i in range(len(nums)):
        x = nums[i]
        if len(nums) - x - 1 >= i:
            edges.append([i, i+x+1])
    for i in range(len(nums)-1,-1,-1):
        x = nums[i]
        if i - x >= 0:
            edges.append([i+1, i-x])
    adj_lists = {i:set() for i in range(len(nums) + 1)}
    for fr, to in edges:
        adj_lists[fr].add(to)
        adj_lists[to].add(fr)
    def dfs(curr):
        if curr == len(nums):
            return True
        while adj_lists[curr]:
            nbr = adj_lists[curr].pop()
            if dfs(nbr): return True
        return False
    print("YES" if dfs(0) else "NO")



    # print(adj_lists)


