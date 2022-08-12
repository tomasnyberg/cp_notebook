from operator import truediv
import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    degree = {j: 0 for j in range(1, n+1)}
    edges = []
    while n > 1:
        fr, to = map(int, lines[i].split(" "))
        degree[fr]+=1
        degree[to]+=1
        edges.append([fr, to])
        n -= 1
        i+=1
    if any([degree[key] >= 3 for key in degree]):
        print(-1)
        continue
    last_taken = {j:-1 for j in range(1, len(degree) + 1)}
    # print(last_taken)
    for fr, to in edges:
        if last_taken[fr] == -1 and last_taken[to] == -1 or (last_taken[fr] == 5 or last_taken[to] == 5):
            last_taken[fr] = 2
            last_taken[to] = 2
            print("weight 2 assigned to edge from", fr, "to", to)
            # print(2, end= " ")
        else:
            last_taken[fr] = 5
            last_taken[to] = 5
            print("weight 5 assigned to edge from", fr, "to", to)
            # print(5, end= " ")
    print()