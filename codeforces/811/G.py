import sys, threading
import bisect
lines = list(map(str.strip, sys.stdin.readlines()))


sys.setrecursionlimit(10**9)
threading.stack_size(10**8)

def solve():
    i = 1
    while i < len(lines):
        n = int(lines[i])
        ncopy = n
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
        result = {}
        taken = []
        def dfs(node, sum):
            # print(node, sum, taken)
            result[node] = bisect.bisect_right(taken, sum)
            if node not in children: return
            for child, left, right in children[node]:
                taken.append((taken[-1] if len(taken) != 0 else 0) + right)
                dfs(child, sum+left)
                taken.pop()
        dfs(1, 0)
        # print()
        for j in range(2, ncopy+1):
            print(result[j], end=" ")
        print()
        # print(traverse_to)
        
threading.Thread(target=solve).start()