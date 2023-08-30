import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    matrix = []
    ii += 1
    for _ in range(n):
        matrix.append(lines[ii])
        ii+=1
    columns = []
    for j in range(m):
        curr = set()
        for i in range(n):
            curr.add(matrix[i][j])
        columns.append(curr)
    target = "vika"
    def check(col):
        curr = 0
        for j in range(col, m):
            if curr == len(target): break
            curr += 1 if target[curr] in columns[j] else 0
        return curr == len(target)
    for j in range(m):
        if check(j):
            print("YES")
            break
    else:
        print("NO")