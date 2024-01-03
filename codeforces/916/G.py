import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n = int(lines[ii])
    nums = list(map(int, lines[ii+1].split()))
    endpoints = {}
    for i, num in enumerate(nums):
        if num not in endpoints:
            endpoints[num] = []
        endpoints[num].append(i)
    inbetween = {}
    allways = {i:set() for i in range(1, n+1)}
    for x in endpoints:
        inbetween[x] = set()
        for i in range(endpoints[x][0]+1, endpoints[x][-1]):
            inbetween[x].add(nums[i])
            allways[x].add(nums[i])
            allways[nums[i]].add(x)
    visited = set()
    curr = []
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        curr.append(node)
        for neighbor in allways[node]:
            if neighbor not in visited:
                dfs(neighbor)
    counts = 0
    groups = []
    for i in range(1, n+1):
        if i not in visited:
            counts += 1
            dfs(i)
            groups.append(curr)
            curr = []
    result = 1
    MOD = 998244353
    visited = set()
    def dfs2(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in inbetween[node]:
            if neighbor not in visited:
                dfs2(neighbor)
    for group in groups:
        count = 0
        for node in group:
            dfs2(node)
            if len(visited) == len(group):
                count += 1
            visited = set()
        result *= count*2
        result %= MOD
    print(len(groups), result)

        
