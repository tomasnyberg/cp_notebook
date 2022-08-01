import sys
lines = list(map(str.strip, sys.stdin.readlines()))



i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    children = {}
    node = 2
    while n > 1:
        parent, a, b = map(int, lines[i].split(" "))
        if parent not in children:
            children[parent] = []
        children[parent].append([node, a, b])
        node += 1
        i+=1
        n-=1
    traverse_to = {}
    def dfs(node, sum, taken):
        traverse_to[node] = (sum, taken)
        if node not in children: return
        for child, left, right in children[node]:
            dfs(child, sum+left, [*taken, right])
    dfs(1, 0, [])
    print(traverse_to)