import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    seen = set()
    for i in range(len(line) - 1):
        seen.add(line[i:i+2])
    print(len(seen))
