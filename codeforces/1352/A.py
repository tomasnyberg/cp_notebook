import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    summands = []
    for i in range(len(line) - 1, -1, -1):
        if line[i] != '0':
            summands.append(line[i] + ('0')*(len(line)-1-i))
    summands = list(map(int, summands))
    summands.sort(key=lambda x:-x)
    print(len(summands))
    for sum in summands:
        print(sum, end=" ")
    print()