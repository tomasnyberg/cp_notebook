import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    result = 0
    curr = 0
    currchar = '0'
    for c in line:
        if c == currchar:
            curr += 1
            result = max(result, curr)
        else:
            currchar = c
            curr = 1
    result = max(result, curr)
    print(result + 1)