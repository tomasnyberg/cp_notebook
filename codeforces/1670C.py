import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 4):
    a = list(map(int, lines[i].split(" ")))
    b = list(map(int, lines[i+1].split(" ")))
    c = list(map(int, lines[i+2].split(" ")))
    adj_lists = {j: set() for j in range(1, len(a) + 1)}
    bad_elems = set()
    for j in range(len(a)):
        if a[j] == b[j]: continue
        if c[j] != 0 or a[j] in bad_elems or b[j] in bad_elems:
            bad_elems.update([a[j], b[j], c[j]])
            continue
        adj_lists[a[j]].add(b[j])
        adj_lists[b[j]].add(a[j])
    def dfs(curr):
        bad_elems.add(curr)
        for nbr in adj_lists[curr]:
            if nbr not in bad_elems:
                bad_elems.add(nbr)
                dfs(nbr)
    result = 1
    # print(a)
    # print(b)
    # print(c)
    # print(adj_lists)
    for j in range(1, len(a) + 1):
        if j not in bad_elems and len(adj_lists[j]) != 0:
            result *= 2
            dfs(j)
    print(result)
    # print()
        



    # print()


