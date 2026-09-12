import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

# k == n then we just need to write the diagonal
# n == k == 3: {1, 2, 3}
# 145
# 627
# 893
# n = 3, k = 4: {1, 2, 5, 3}
# 124
# 567
# 893
# n = 3, k = 5: {1, 4, 5, 2, 3}
# 123
# 647
# 895
# n = 3, k = 6: {1, 4, 7, 2, 3}
# 123
# 456
# 789
# hypothesis: Can get at most n*2 -1
def check(expected, result):
    seen = set()
    for row in result:
        seen.add(min(row))
    for col in range(len(result)):
        seen.add(min(result[i][col] for i in range(len(result))))
    assert len(seen) == expected

for line in lines[1:]:
    n, k = map(int, line.split())
    if k < n or k == 2*n:
        print(-1)
        continue
    extra = k - n + 1
    result = [[0]*n for _ in range(n)]
    curr = 1
    for i in range(extra):
        result[0][i] = curr
        curr+=1
    for i in range(1, n):
        result[i][i] = curr
        curr+=1
    for i in range(n):
        for j in range(n):
            if result[i][j] == 0:
                result[i][j] = curr
                curr += 1
    # check(k, result)
    for xs in result:
        print(*xs)


