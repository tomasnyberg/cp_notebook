import sys
lines = list(map(str.strip, sys.stdin.readlines()))

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split(" "))
    ii+=1
    adj_lists = {ii: [] for ii in range(1, n+1)}
    for _ in range(m):
        fr, to = map(int, lines[ii].split(" "))
        adj_lists[fr].append(to)
        adj_lists[to].append(fr)
        ii+=1
    third = -1
    for i in range(1, n+1):
        if len(adj_lists[i]) == 1:
            third = i
            break
    second = adj_lists[third][0]
    first = -1
    for nbr in adj_lists[second]:
        if len(adj_lists[nbr]) != 1:
            first = nbr
            break
    print(len(adj_lists[first]), len(adj_lists[second]) - 1)