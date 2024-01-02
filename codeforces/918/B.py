import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    matrix = [lines[ii], lines[ii+1], lines[ii+2]]
    for line in matrix:
        if line.count('?') == 1:
            expected = set(['A', 'B', 'C'])
            print((expected - set(line)).pop())
            
