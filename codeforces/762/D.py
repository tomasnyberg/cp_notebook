import sys
lines = list(map(str.strip, sys.stdin.readlines()))

a = 2
while a < len(lines):
    m, n = map(int, lines[a].split(" "))
    a+=1
    ncopy = m
    matrix = []
    while ncopy > 0:
        matrix.append(list(map(int, lines[a].split(" "))))
        ncopy-=1
        a+=1
    a+=1
    beststore = {i: [] for i in range(n)} # friend -> [score, store, secondbest]
    for i in range(m):
        for j in range(n):
            if not beststore[j] or matrix[i][j] > beststore[j][0]:
                last = -1 if not beststore[j] else beststore[j][2]
                beststore[j] = [matrix[i][j], i, last]
            elif beststore[j][2] < matrix[i][j]:
                beststore[j][2] = matrix[i][j]
    stores = set()
    # print(beststore)
    beststore = [beststore[key] for key in beststore]
    for score, store, secondbest in beststore:
        stores.add(store)
    if len(stores) <= n - 1:
        print(min([score for score, store, secondbest in beststore]))
    else:
        print(max([secondbest for score, store, secondbest in beststore]))