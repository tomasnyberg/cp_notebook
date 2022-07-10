import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    powers_of_ten = len(line) - 1
    n = int(line)
    print(n - (10**powers_of_ten))