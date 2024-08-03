import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


def f(i, k, xs):
    tot = 0
    for j in range(i):
        if xs[j] >= k:
            tot += xs[j]
    return tot


def g(i, m, xs):
    tot = 0
    for j in range(i):
        if xs[j] <= m:
            tot += xs[j]
    return tot


def test(xs, m, k):
    result = 0
    for i in range(1, len(xs) + 1):
        result += f(i, k, xs) - g(i, m, xs)
    return result


for line in lines[1:]:
    n, m, k = map(int, line.split())
    perm = list(range(n, 0, -1))
    result = []
    while n >= k or n > m:
        result.append(n)
        n -= 1
    result += list(range(1, n+1))
    print(*result)
