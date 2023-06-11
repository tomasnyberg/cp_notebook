import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def try_replace(start, end, line):
    biggest = [-1,-1]
    for replacement in ['0', '1']:
        for i in range(start, end):
            line[i] = replacement
        count = 0
        left = start
        right = start + 1
        while left >= 0:
            if line[left] != replacement:
                break
            count += 1
            left -= 1
        while right < len(line):
            if line[right] != replacement:
                break
            count += 1
            right += 1
        biggest = max(biggest, [count, replacement])
    for i in range(start, end):
        line[i] = biggest[1]

for line in lines[1:]:
    i = 0
    line = list(line)
    while i < len(line):
        if line[i] != '?':
            i += 1
            continue
        j = i
        while i < len(line) and line[i] == '?':
            i += 1
        try_replace(j, i, line)
    print(''.join(line))
        