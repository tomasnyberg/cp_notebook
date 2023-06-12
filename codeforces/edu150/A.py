import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    if n <= 4:
        print("Bob")
    else:
        print("Alice")