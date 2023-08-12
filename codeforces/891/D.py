import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for i in range(1, len(lines), 3):
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    diffs = [a[i] - b[i] for i in range(len(a))]
    diffs = list(enumerate(diffs))
    diffs.sort(key=lambda x: x[1])
    big = diffs[-1][1]
    result = []
    while diffs and diffs[-1][1] == big:
        i, _ = diffs.pop()
        result.append(i + 1)
    result.sort()
    print(len(result))
    print(*result)