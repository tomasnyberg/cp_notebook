import random

N = 100

def generate_tree(n):
    nodes = list(range(1, n + 1))
    random.shuffle(nodes)
    parent = {nodes[0]: None}
    for node in nodes[1:]:
        parent[node] = random.choice(list(parent.keys()))
    print(n)
    for node, parentNode in parent.items():
        if parentNode is not None:
            print(parentNode, node)
            
print(N)
for i in range(N):
    generate_tree(9)