import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque
from itertools import permutations


def brute_force(s):
    # Check all permutations of s
    s = list(s)
    seen = set()
    for p in permutations(s):
        a = p
        b = p[::-1]
        seen.add(max(a, b))
    return "".join(min(seen))

for line in lines[1:]:
    org = line
    line = list(line)
    counts = {}
    for c in line:
        counts[c] = counts.get(c, 0) + 1
    left = ""
    right = ""
    all_right = False
    put_in_middle = False
    for c in range(97, 97+26):
        orded = chr(c)
        if orded not in counts: continue
        if all_right:
            right += chr(c) * counts[orded]
            continue
        while counts[orded] > 1:
            left += chr(c)
            right += chr(c)
            counts[orded] -= 2
        if counts[orded] == 1:
            if put_in_middle:
                right += chr(c)
                break
            remaining = sum(1 for x in range(c + 1, 97 + 26) if chr(x) in counts)
            if remaining > 1:
                left += chr(c)
                all_right = True
            else:
                put_in_middle = chr(c)
    if put_in_middle:
        left += put_in_middle
    res = left + right[::-1]
    print(max(res, res[::-1]))
    