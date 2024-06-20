import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, m = map(int, lines[ii].split())
    probs = lines[ii+1]
    counts = [0]*7
    for c in probs:
        counts[ord(c) - ord('A')] += 1
    result = 0
    for x in counts:
        result += max(0, m - x)
    print(result)
