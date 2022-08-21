import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    counts = {}
    for c in line:
        counts[c] = 1 if c not in counts else counts[c] + 1
    print("YES" if (counts['A'] if 'A' in counts else 0) + (counts['C'] if 'C' in counts else 0) == (counts['B'] if 'B' in counts else 0) else "NO")