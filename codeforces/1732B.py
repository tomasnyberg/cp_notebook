import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    count = 0
    prev = 0
    for i in range(len(line)):
        if int(line[i]) != prev:
            count += 1
        prev = int(line[i])
    print(max(0, count-1))
