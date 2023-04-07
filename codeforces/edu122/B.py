import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    ones = line.count('1')
    zeroes = line.count('0')
    # print(line)
    # print(ones, zeroes)
    print(min(ones, zeroes) if ones != zeroes else min(ones, zeroes) - 1)