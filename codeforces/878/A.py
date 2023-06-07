import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    i = 0
    result = ""
    while i < len(line):
        curr = line[i]
        result += curr
        i+=1
        while i < len(line) and line[i] != curr:
            i+=1
        i+=1
    print(result)