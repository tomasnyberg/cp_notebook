import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    print("YES" if line in "codeforces" else "NO")