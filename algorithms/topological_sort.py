# Explanation : https://www.youtube.com/watch?v=eL-KzMXSXXI

example = {1: [3], 2: [3, 4], 3: [], 4: [], 5: [], 6: [2, 3], 7: [1, 2, 3]}
example2 = {'a':['d'], 'b':['d'], 'c':['a','b'], 'd': ['h', 'g'], 'e':['a','d','f'],
'f':['j', 'k'], 'g':['i'], 'h':['i', 'j'], 'i':['l'], 'j':['m', 'l'], 'k':['j'], 'l':[], 'm':[]}
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
    for key in adj_lists:
        if key not in visited:
            dfs(key, result)
    result.reverse()
    return result    

for key in topological_sort(13, example2):
    print(key, example2[key])
