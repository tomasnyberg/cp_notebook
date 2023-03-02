import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    bad = set()
    result = 0
    for i in range(2, len(line)):
        if line[i-2] != line[i]:
            result += 1
    print(result + 1)
