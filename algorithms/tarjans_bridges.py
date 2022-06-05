# Example taken from https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png
# The edge [1,3] is a critical edge
example_adj_lists = {0: [1, 2], 1: [0, 2, 3], 2: [1, 0], 3: [1]}

# Finds the bridges in a graph that, if removed, increase the number of SCCS in a graph
# Used in for example leetcode 1192
# Time complexity: O(V + E)
def tarjans_bridges(adj_lists):
    n = len(adj_lists)
    parents = [-1]*n
    disc = [-1]*n
    low = [-1]*n
    time = [0]
    result = []
    def dfs(n):
        low[n] = time[0]
        disc[n] = time[0]
        time[0] += 1
        for nbr in adj_lists[n]:
            if parents[n] != nbr:
                if disc[nbr] == -1:
                    parents[nbr] = n
                    dfs(nbr)
                low[n] = min(low[n], low[nbr])
            if low[nbr] > disc[n]:
                result.append([n, nbr])
    dfs(0)
    return result

print(tarjans_bridges(example_adj_lists))