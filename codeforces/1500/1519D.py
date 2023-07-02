import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))

# lines = """5
# 2 3 2 1 3
# 1 3 2 4 2
# 2
# 13 37
# 2 4
# 6
# 1 8 7 6 3 6
# 5 9 6 8 8 6""".split("\n")


# 
# 1 2 8 7 4 3 2 1
# 5 2 7 2 6 8 9 5

for ii in range(1, len(lines), 3):
    a = list(map(int, lines[ii].split()))
    b = list(map(int, lines[ii+1].split()))
    @lru_cache(None)
    def expand(left, right):
        if left < 0 or right == len(a):
            return 0
        curr =  a[right] * b[left] + a[left] * b[right] 
        prev = a[right] * b[right] + a[left] * b[left]
        keep_going = expand(left-1, right+1)
        return max(keep_going + curr - prev, curr - prev)
    max_inc = 0
    for i in range(len(a) - 1):
        max_inc = max(max_inc, expand(i, i+1), expand(i, i))
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    print(result + max_inc)


