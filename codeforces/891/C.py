import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import Counter
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    d = dict(Counter(nums))
    items = list(d.items())
    items.sort(key=lambda x: x[0], reverse=True)
    # print(items)
    result = [10**9]
    for i in range(len(items)):
        elem, count = items[i]
        while count > 0:
            count -= len(result)
            result.append(elem)
    print(*result)