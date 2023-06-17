import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

# lines = """2
# 4
# 1001
# 1
# 0
# 5
# 10010""".split("\n")

for s in lines[2::2]:
    if s == s[::-1]:
        if len(s) % 2 == 1 and s[len(s) // 2] == '0' and len(s) > 1 and s.count('0') > 1:
            print("ALICE")
        else:
            print("BOB")
        continue
    if s.count('0') == 2 and len(s) % 2 == 1 and s[len(s) // 2] == '0':
        print("DRAW")
        continue
    print("ALICE")