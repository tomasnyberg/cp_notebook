from functools import lru_cache

def solve(n, k, p):
    p = [0] + p
    for i in range(1, len(p)):
        p[i] -= 1
    # Find all the leaves in the tree given the parent array
    def find_leaves(p):
        pointed_to = [0] * len(p)
        for i in range(1, len(p)):
            pointed_to[p[i]] += 1
        leaves = []
        for i in range(len(p)):
            if pointed_to[i] == 0:
                leaves.append(i)
        return leaves
    leaves = set(find_leaves(p))
    # print(p)
    def check(parents, mid):
        parents = parents.copy()
        removed = set()
        def walk_tree(i):
            ops = 0
            stack = []
            while i != 0:
                if i in removed:
                    return ops
                stack.append(i)
                if len(stack) == mid and parents[i] != 0:
                    for j in stack:
                        removed.add(j)
                    ops += 1
                    # print("current stack", stack, "node", i, "parent", parents[i])
                    stack = []
                i = parents[i]
            return ops
        walks = [walk_tree(i) for i in range(n) if i in leaves]
        # print(walks)
        return sum(walks) <= k  
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        res = check(p, mid)
        # print(mid, res)
        if res:
            high = mid
        else:
            low = mid + 1
    # print("----\n\n")
    return low

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, k, p))
