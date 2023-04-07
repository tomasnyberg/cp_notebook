import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

i = 1
while i < len(lines):
    n, m=  map(int, lines[i].split(" "))
    matrix = []
    i+=1
    while n > 0:
        matrix.append(list(map(lambda x: 1 if x == '*' else 0, lines[i])))
        i+=1
        n-=1
    css = []
    for xs in matrix:
        css.append(cum_sum(xs))
    result = 0
    for j in range(len(matrix)):
        for k in range(len(matrix[0])):
            if not matrix[j][k]: continue
            left = k
            right = k
            row = j
            height = 0
            while row < len(matrix) and left >= 0 and right < len(matrix[0]):
                if css[row][right] - css[row][left] == right - left and matrix[row][left] and matrix[row][right]:
                    height += 1
                    left -= 1
                    right += 1
                    row+=1
                else:
                    break
            result += height
            # print("node at", j, k, "is part of a tree of height", height)
    print(result)
    # for xs in css:
    #     [print(x, end=" ") for x in xs]
    #     print()
