import sys
from collections import defaultdict, Counter
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 4):
    n, m = map(int, lines[ii].split())
    s = lines[ii+1]
    indices = list(map(int, lines[ii+2].split()))
    replacements = list(lines[ii+3])
    replacements.sort(key=lambda x: ord(x))
    indices.sort(reverse=True)
    index_to_replacements = defaultdict(list)
    index_counts = Counter(indices)
    i = len(replacements) - 1
    j = 0
    for idx, amount in sorted(index_counts.items(), key=lambda x: x[0]):
        for _ in range(amount - 1):
            index_to_replacements[idx-1].append(replacements[i])
            i -= 1
        index_to_replacements[idx-1].append(replacements[j])
        j += 1
    s = list(s)
    for i in range(n):
        for replacement in index_to_replacements[i]:
            s[i] = replacement
    print(''.join(s))
