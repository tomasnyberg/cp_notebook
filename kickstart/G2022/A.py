import sys
lines = list(map(str.strip, sys.stdin.readlines()))

test = 1
i = 1
while i < len(lines):
    m, n, p = map(int, lines[i].split(" "))
    i+=1
    matrix = []
    while m > 0:
        matrix.append(list(map(int, lines[i].split(" "))))
        i+=1
        m-=1
    result = 0
    for col in range(len(matrix[0])):
        johnscore = matrix[p-1][col]
        biggest = 0
        for row in range(len(matrix)):
            biggest = max(matrix[row][col], biggest)
        result += biggest - johnscore
    print(f"Case #{test}:", result)
    test+=1
