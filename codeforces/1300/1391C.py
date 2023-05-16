import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from itertools import permutations

def has_cycle(adj_list):
    visited = set()

    def dfs(node, parent, depth):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                if dfs(neighbor, node, depth + 1):
                    return True
            elif parent != neighbor and depth >= 2:  # depth of 2 corresponds to cycle of length 3
                return True
        return False

    for node in adj_list:
        if node not in visited:
            if dfs(node, None, 0):
                return True

    return False

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        result %= 10**9 + 7
    return result

def brute_force(l):
    p = [i for i in range(1, l+1)]
    count = 0
    for perm in permutations(p):
        adj_lists = {i: [] for i in range(len(perm))}
        for i in range(len(perm)):
            ptr = i - 1
            while ptr >= 0:
                if perm[ptr] > perm[i]:
                    adj_lists[i].append(ptr)
                    adj_lists[ptr].append(i)
                    break
                ptr -= 1
            ptr = i+1
            while ptr < len(perm):
                if perm[ptr] > perm[i]:
                    adj_lists[i].append(ptr)
                    adj_lists[ptr].append(i)
                    break
                ptr += 1
        if has_cycle(adj_lists):
            count += 1
    return count

# for l in range(3,9):
#     bf = brute_force(l)
#     print(l, bf, factorial(l), factorial(l) - bf)
#     # print(has_cycle(perm))

n = int(lines[0])
print((factorial(n) - pow(2, n-1, 10**9 + 7)) % (10**9 + 7))