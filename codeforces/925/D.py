import sys
from collections import defaultdict
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, x, y = map(int, lines[ii].split())
    nums = list(map(int, lines[ii + 1].split()))
    seen = defaultdict(int)
    xmodded = [num % x for num in nums]
    ymodded = [num % y for num in nums]
    result = 0
    for i, (xmod, ymod) in enumerate(zip(xmodded, ymodded)):
        xneeded = (x - xmod) % x
        yneeded = ymod
        tup = (xneeded, yneeded)
        result += seen[tup]
        seen[(xmod, ymod)] += 1
    print(result)
