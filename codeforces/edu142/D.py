import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def permutation_product(p, q):
    n = len(p)
    product = [0] * n
    for o in range(n):
        product[o] = q[p[o]-1]
    return product

def beauty(arr):
    result = 0
    for o in range(len(arr)):
        if arr[o] == o + 1:
            result += 1
        else:
            break
    return result

o = 1
while o < len(lines):
    n, m = map(int, lines[o].split())
    arrays = []
    for j in range(n):
        arrays.append(list(map(int, lines[o + j + 1].split())))
    o += n + 1
    for i in range(len(arrays)):
        result = 0
        for j in range(len(arrays)):
            result = max(result, beauty(permutation_product(arrays[i], arrays[j])))
        print(result, end=' ')
    print()
            
