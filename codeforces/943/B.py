import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    a = lines[ii+1]
    b = lines[ii+2]
    i = 0
    for c in b:
        if c == a[i]:
            i += 1
        if i == len(a):
            break
    print(i)