import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

def check(s, i, j):
    startsame = i == j
    to_right = len(s) - j
    to_left = i + 1
    a = ""
    b = ""
    result = 0
    while i >= 0 and j < len(s) and s[i] == s[j]:
        a += s[i]
        b += s[j]
        i -= 1
        j += 1
        to_right -=1
        to_left -= 1
    if i == -1 or j == len(s):
        while i >= 0:
            i -= 1
            result += 1
        while j < len(s):
            j += 1
            result += 1
        return result
    while to_right > to_left:
        j+=1
        result += 1
        to_right -= 1
    while to_left > to_right:
        i -= 1
        result += 1
        to_left -= 1
    while i >= 0 and j < len(s):
        a += s[i]
        b += s[j]
        i -= 1
        j += 1
    return result if a == b else 10**9

for s in lines:
    if s == s[::-1]:
        print(s)
        continue
    least = [10**9, 0, 0]
    for i in range(len(s) - 1):
        least = min(least, [check(s, i, i), i, i])
        if s[i] == s[i+1]:
            least = min(least, [check(s, i, i+1), i, i+1])
    print(least)
        

    



        