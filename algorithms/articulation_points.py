
# Example adj list, 3,4,5,10,12 are articulation points
# Taken from https://en.wikipedia.org/wiki/Biconnected_component#/media/File:TarjanAPDemoDepth.gif
adj_lists = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2,4], 4:[3,5], 5:[4,10], 
             6:[7,8,10], 7:[6,8], 8:[6,7,9], 9:[8,12], 10:[5,6,11,12],
             11:[10], 12:[9,10,13], 13:[12]}

def find_APS(adj_lists):
    n = len(adj_lists)
    disc = [-1]*n
    parents = [-1]*n
    low = [-1]*n
    sum_parent_to = [0]*n
    time = [0]
    def dfs(n):
        disc[n] = time[0]
        low[n] = time[0]
        time[0] += 1
        for nbr in adj_lists[n]:
            if parents[n] != nbr:
                if disc[nbr] == -1:
                    sum_parent_to[n] += 1
                    parents[nbr] = n
                    dfs(nbr)
                low[n] = min(low[n], low[nbr])
    dfs(0)
    result = set()
    # Node has two unique children and dfs started from it 
    for idx, spt in enumerate(sum_parent_to):
        if spt >= 2 and disc[idx] == low[idx]:
            result.add(idx)
    # Low link of the child node is less than its parent
    # This means there is no way to reach the child without
    # going through the parent node, i.e. the parent is an AP
    for idx, parent in enumerate(parents):
        if low[idx] > low[parent]:
            result.add(parent)
    return result
print(find_APS(adj_lists))
