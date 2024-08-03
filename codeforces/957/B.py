import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    xs = list(map(int, lines[ii+1].split()))
    biggest_idx = xs.index(max(xs))
    # Add them back to the biggest one
    result = n - xs[biggest_idx]
    for i in range(k):
        if i != biggest_idx:
            result += xs[i] - 1
    print(result)
