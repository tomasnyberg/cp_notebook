import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def try_replace(start, end, line):
    total = 0
    if start > 0:
        total += line[start-1]
    if end < len(line):
        total += line[end]
    replacer = '.'
    if total >= 0:
        replacer = 1
    else:
        replacer = -1
    for i in range(start, end):
        line[i] = replacer
        
for line in lines[1:]:
    i = 0
    line = list(line)
    curr = '.'
    count = 0
    for i in range(len(line)):
        if line[i] == '?':
            j = i - 1
            for j in range(i-1, i - 1- count, -1):
                line[j] = count if curr == '0' else -count
            count = 0
            curr = '.'
            continue
        elif line[i] == curr:
            count += 1
        else:
            j = i - 1
            for j in range(i-1, i - 1- count, -1):
                line[j] = count if curr == '0' else -count
            count = 1
            curr = line[i]
    i = len(line)
    j = i - 1
    for j in range(i-1, i - 1- count, -1):
        line[j] = count if curr == '0' else -count
    i = 0
    while i < len(line):
        if line[i] != '?':
            i += 1
            continue
        j = i
        while i < len(line) and line[i] == '?':
            i += 1
        try_replace(j, i, line)
    for i in range(len(line)):
        if line[i] < 0:
            line[i] = '1'
        else:
            line[i] = '0'
    print(''.join(line))
        