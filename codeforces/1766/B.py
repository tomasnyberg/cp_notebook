import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, s = lines[i], lines[i+1]
    seen = {}
    good = False
    for i in range(len(s) - 1):
        if s[i:i+2] in seen:
            if seen[s[i:i+2]] != i-1:
                good = True
                break
        else:
            seen[s[i:i+2]] = i
    print("YES" if good else "NO")
