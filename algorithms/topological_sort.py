# Explanation : https://www.youtube.com/watch?v=eL-KzMXSXXI

example = {1: [3], 2: [3, 4], 3: [], 4: [], 5: [], 6: [2, 3], 7: [1, 2, 3]}

def topological_sort(n, adj_lists):
    visited = set()
    result = []
    def dfs(curr, result):
        visited.add(curr)
        for nbr in adj_lists[curr]:
            if nbr in visited:
                continue
            dfs(nbr, result)
        result.append(curr)
    for i in range(1, n + 1):
        if i not in visited:
            dfs(i, result)
    result.reverse()
    return result    

print(topological_sort(7, example))