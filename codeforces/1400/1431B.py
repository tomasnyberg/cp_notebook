import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    split = line.split("w")
    result = sum([1 if c == 'w' else 0 for c in line])
    for part in split:
        result += len(part)//2
    print(result)

    