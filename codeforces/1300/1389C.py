import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import random

def good(s):
    return s[1:] + s[0] == s[-1] + s[:-1]

chars = [str(i) for i in range(10)]
# for _ in range(1000000):
#     curr = ""
#     for i in range(8):
#         curr += random.choice(chars)
#     if good(curr):
#         print(curr)

for s in lines[1:]:
    counts = {}
    result = len(s)
    for c in s:
        counts[c] = 1 if c not in counts else counts[c] + 1
    for c in counts:
        result = min(result, len(s) - counts[c])
    pairs = {}
    for i in range(10):
        for j in range(10):
            pairs[(i, j)] = -10**9# Positive if looking for the first, negative if looking for the second
    for c in s:
        c = int(c)
        for i in range(10):
            if i == c: continue
            if pairs[(i, c)] >= 0:
                pairs[(i, c)] = -pairs[(i, c)] - 1
        for i in range(10):
            if i == c: continue
            if pairs[(c, i)] == -10**9:
                pairs[(c, i)] = 0
            pairs[(c, i)] = abs(pairs[(c, i)])
    for key in pairs:
        if abs(pairs[key]) != 0 and abs(pairs[key]) != 10**9:
            # print(key, pairs[key])
            result = min(result, len(s) - 2*abs(pairs[key]))
    print(result)
    

