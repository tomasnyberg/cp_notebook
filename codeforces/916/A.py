import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

expected = [i+1 for i in range(26)]
for line in lines[2::2]:
    counts = [0]*26
    for c in line:
        counts[ord(c)-ord('A')] += 1
    result = 0
    for x, y in zip(counts, expected):
        result += 1 if x >= y else 0
    print(result)