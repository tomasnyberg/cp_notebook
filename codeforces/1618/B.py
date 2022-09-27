import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    split = line.split(" ")
    result = split[0]
    found = False
    for i in range(1, len(split)):
        if split[i][0] != split[i-1][1]:
            result += split[i][0]
            found = True
        result += split[i][1]
    if not found:
        result += split[-1][1]
    print(result)