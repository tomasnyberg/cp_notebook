import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    alphabetical = list(sorted(set(line)))
    indices = {c: i for i, c in enumerate(alphabetical)}
    for c in line:
        print(alphabetical[len(alphabetical) - indices[c] - 1], end='')
    print()
