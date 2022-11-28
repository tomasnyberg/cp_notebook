import sys
lines = list(map(str.strip, sys.stdin.readlines()))

p1result = 0
p2result = 0
for line in lines:
    num, password = line.split(": ")
    numrange, letter = num.split(" ")
    fr, to = map(int, numrange.split("-"))
    if fr <= sum(1 for char in password if char == letter) <= to:
        p1result += 1
    count = 0
    if password[fr-1] == letter: count +=1
    if password[to-1] == letter: count += 1
    if count == 1: p2result += 1

print("Part one: ", p1result)
print("Part two: ", p2result)
