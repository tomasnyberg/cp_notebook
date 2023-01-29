import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def f(x):
    result = 0
    while x > 0:
        result += 1
        x //= 10
    return result

def remove_matches(a, b):
    a_counts = {}
    b_counts = {}
    for x in a:
        a_counts[x] = a_counts.get(x, 0) + 1
    for x in b:
        b_counts[x] = b_counts.get(x, 0) + 1
    result_a = []
    result_b = []
    for x in a_counts:
        if x in b_counts:
            count = min(a_counts[x], b_counts[x])
            a_counts[x] -= count
            b_counts[x] -= count
    for x in a_counts:
        result_a += [x] * a_counts[x]
    for x in b_counts:
        result_b += [x] * b_counts[x]
    assert len(result_a) == len(result_b)
    return result_a, result_b

for i in range(1, len(lines), 3):
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    a, b = remove_matches(a, b)
    result = 0
    for i in range(len(a)):
        for arr in [a, b]:
            if arr[i] > 9:
                arr[i] = f(arr[i])
                result += 1
    a, b = remove_matches(a, b)
    for i in range(len(a)):
        for arr in [a, b]:
            if arr[i] > 1:
                arr[i] = f(arr[i])
                result += 1
    print(result)
    # print(a)
    # print(b)