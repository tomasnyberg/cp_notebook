# example taken from https://leetcode.com/problems/reconstruct-itinerary/
example = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

# NOTE: you might need to find which node is the starting node first.
# This is the node has one more outgoing edge than incoming edge.
# This algorithm also assumes that the graph is directed.
def eulerian_path(edges, start):
    adj_lists = {}
    for fr, to in edges[::-1]:
        if fr not in adj_lists: adj_lists[fr] = []
        adj_lists[fr].append(to)
    result = []
    def dfs(curr):
        while curr in adj_lists and adj_lists[curr]:
            dfs(adj_lists[curr].pop())
        result.append(curr)
    dfs(start)
    return result[::-1] # reverse since otherwise you get the last node first

print(eulerian_path(example, "JFK"))
