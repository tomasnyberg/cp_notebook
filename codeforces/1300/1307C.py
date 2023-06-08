import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import Counter

def combo_breaker(s, combo):
    firstseen = 0
    result = 0
    for c in s:
        if c == combo[1]:
            result += firstseen
        if c == combo[0]:
            firstseen += 1
    return result

for s in lines:
    d = dict(Counter(s))
    result = max(d.values())
    for i in range(26):
        for j in range(26):
            first = chr(ord('a') + i)
            second = chr(ord('a') + j)
            result = max(result, combo_breaker(s, (first, second)))
    print(result)
            
