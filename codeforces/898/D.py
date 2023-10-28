import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    s = lines[ii+1]
    result = 0
    good_for = 0
    for i, c in enumerate(s):
        if good_for > 0:
            good_for -= 1
            continue
        if c == 'B':
            result += 1
            good_for = k-1
    print(result)

    