import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n = int(lines[i])
    matrix = []
    i+=1
    while n > 0:
        matrix.append(list(lines[i]))
        n-=1
        i+=1
    points = []
    for j in range(len(matrix)):
        for k in range(len(matrix)):
            if matrix[j][k] == '*':
                points.append([j, k])
    points.sort(key= lambda x: x[1])
    if points[0][0] == points[1][0]:
        row = points[0][0]
        if row > 0:
            matrix[row-1][points[0][1]] = '*'
            matrix[row-1][points[1][1]] = '*'
        else:
            matrix[1][points[0][1]] = '*'
            matrix[1][points[1][1]] = '*'
    elif points[0][1] == points[1][1]:
        col = points[0][1]
        if col > 0:
            matrix[points[0][0]][col-1] = '*'
            matrix[points[1][0]][col-1] = '*'
        else:
            matrix[points[0][0]][1] = '*'
            matrix[points[1][0]][1] = '*'
    else:
        matrix[points[0][0]][points[1][1]] ='*'
        matrix[points[1][0]][points[0][1]] = '*'
    for xs in matrix:
        for x in xs:
            print(x, end="")
        print()
        
        