import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    running = ""
    result = 0
    for x in bin(int(line))[2:]:
        running += x
        result += int(running, 2)
    print(result)
        