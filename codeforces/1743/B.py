import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    print(*([1,int(line)] + [i for i in range(2,int(line))]))
