import sys
from math import ceil
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    waiting = {'a': 0, 'b': 0}
    unknown = 0
    result = 0
    for x in nums:
        if x == 1:
            unknown += 1
            result = max(result, ceil(waiting['a']/2) + ceil(waiting['b']/2) + unknown)
        elif x == 2:
            waiting['a'] += (unknown // 2)
            waiting['b'] += (unknown // 2)
            if waiting['a'] % 2 == 0:
                waiting['a'] += unknown % 2
            else:
                waiting['b'] += unknown % 2
            unknown = 0
    # print(unknown, result, waiting)
    print(max(ceil(waiting['a']/2) + ceil(waiting['b']/2) + unknown, result))



    # print(result + running)