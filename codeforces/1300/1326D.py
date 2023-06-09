import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

def manacher(s):
    s = '#'.join('^{}$'.format(s))
    n = len(s)
    P = [0] * n
    C = R = 0
    for i in range(1, n-1):
        if R > i:
            i_mirror = 2*C - i  # i's mirror position in the previously calculated palindrome
            P[i] = min(R-i, P[i_mirror])  # Truncate P[i] at R if it overflows
        # Attempt to expand
        while s[i + 1 + P[i]] == s[i - 1 - P[i]]:
            P[i] += 1
        # Update C and R if i's palindrome expands past R
        if i + P[i] > R:
            C, R = i, i + P[i]
    best = [-1,-1]
    for i in range(1, n-1):
        if P[i] > best[0] and (i - P[i] == 1 or P[i] + i == len(P) - 2):
            best = [P[i], i]
    max_length, center_index = best
    return s[center_index - max_length:center_index + max_length].replace("#", "")

for s in lines[1:]:
    if s == s[::-1]:
        print(s)
        continue
    start = ""
    end = ""
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            break
        start += s[i]
        end += s[j]
        i += 1
        j -= 1
    end = end[::-1]
    middle = manacher(s[i:j+1])
    print(start + middle + end)