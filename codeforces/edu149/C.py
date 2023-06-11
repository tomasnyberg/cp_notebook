import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    line = list(line)
    if line[0] == '?':
        line[0] = '0'
    for i in range(1, len(line)):
        if line[i] == '?':
            line[i] = line[i-1]
    print(''.join(line))
        