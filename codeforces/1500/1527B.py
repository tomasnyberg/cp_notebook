import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

sys.setrecursionlimit(10**4)

@lru_cache(None)
def solve(symmetric_0, nonsymmetric, mid, prev_rev):
    if symmetric_0 == nonsymmetric == 0 and not mid:
        return 0
    result = 10**9
    if not prev_rev and nonsymmetric > 0:
        result = min(result, -solve(symmetric_0, nonsymmetric, mid, True))
    if symmetric_0 > 0:
        result = min(result, 1 - solve(symmetric_0 - 1, nonsymmetric + 1, mid, False))
    if nonsymmetric > 0:
        result = min(result, 1 - solve(symmetric_0, nonsymmetric - 1, mid, False))
    if mid:
        result = min(result, 1 - solve(symmetric_0, nonsymmetric, False, False))
    return result

for s in lines[2::2]:
    if s == s[::-1]:
        if len(s) % 2 == 1 and s[len(s) // 2] == '0' and len(s) > 1 and s.count('0') > 1:
            print("ALICE")
        else:
            print("BOB")
        continue
    symmetric_0 = nonsymmetric = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1] and s[i] == '0':
            symmetric_0 += 1
        elif s[i] != s[len(s) - i - 1]:
            nonsymmetric += 1
    mid = len(s) % 2 == 1 and s[len(s) // 2] == '0'
    res = solve(symmetric_0, nonsymmetric, mid, False)
    print("ALICE" if res < 0 else "BOB" if res > 0 else "DRAW")
