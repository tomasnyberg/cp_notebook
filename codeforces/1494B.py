from multiprocessing.context import assert_spawning
import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, U, R, D, L = map(int, line.split(" "))
    assignments = [False, False, False, False]
    neededcorners = []
    atmostcorners = []
    for dir in [U, R, D, L]:
        neededcorners.append(2 if dir == n else (1 if dir == n-1 else 0))
    for dir in [U, R, D, L]:
        atmostcorners.append(10**9 if dir >= 2 else dir)
        
    
    # print(neededcorners)
    # print(atmostcorners)
    def dfs(assigned, i):
        if i == len(assigned):
            corners = [0, 0, 0, 0]
            corners[0] = assigned[0] + assigned[1]
            corners[1] = assigned[1] + assigned[2]
            corners[2] = assigned[2] + assigned[3]
            corners[3] = assigned[3] + assigned[0]
            for j in range(len(corners)):
                if corners[j] < neededcorners[j] or corners[j] > atmostcorners[j]:
                    return False
            return True
        a = dfs([*assigned], i+1)
        assigned[i] = 1
        b = dfs([*assigned], i+1)
        return a or b
    print("YES" if dfs([0, 0, 0, 0], 0) else "NO")