import sys
from decimal import Decimal, getcontext

def query(x, y):
    print("?", x, y)
    sys.stdout.flush()
    return int(input())

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    first = query(1, 1)
    second_query = (min(n, 1 + first), min(m, 1 + first))
    second = query(*second_query)
    # The node second positions up from the second_query
    up = (second_query[0] - second, second_query[1])
    if up[0] < 1:
        up = (1, up[1])
    # The node second positions left from the second_query
    left = (second_query[0], second_query[1] - second)
    if left[1] < 1:
        left = (left[0], 1)
    third = query(*up)
    if third == 0:
        print("!", *up)
    else:
        print("!", *left)
    sys.stdout.flush()
# Choose three non-collinear points A, B, and C based on the dimensions
    

