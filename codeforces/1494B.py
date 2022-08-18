import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, U, R, D, L = map(int, line.split(" "))
    neededcorners = []
    atmostcorners = []
    for dir in [U, R, D, L]:
        neededcorners.append(2 if dir == n else (1 if dir == n-1 else 0))
        atmostcorners.append(10**9 if dir >= 2 else dir)
    def dfs(assigned, i):
        if i == len(assigned):
            corners = [0, 0, 0, 0]
            for j in range(len(corners)):
                corners[j] = assigned[j] + assigned[(j+1)%len(corners)]
            for j in range(len(corners)):
                if corners[j] < neededcorners[j] or corners[j] > atmostcorners[j]:
                    return False
            return True
        a = dfs([*assigned], i+1)
        assigned[i] = 1
        b = dfs([*assigned], i+1)
        return a or b
    print("YES" if dfs([0, 0, 0, 0], 0) else "NO")