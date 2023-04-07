import sys
lines = list(map(str.strip, sys.stdin.readlines()))

threechar = set(['aba', 'aca'])
fourchar = set(['abca', 'acba'])
sevenchar = set(['abbacca', 'accabba'])
for line in lines[2::2]:
    shortest = 10
    for i in range(len(line)):
        if i+2 <= len(line) and line[i:i+2] == 'aa':
            shortest = 2
        if i+3 <= len(line) and line[i:i+3] in threechar:
            shortest = min(shortest, 3) 
        if i+4 <= len(line) and line[i:i+4] in fourchar:
            shortest = min(shortest, 4)
        if i+7 <= len(line) and line[i:i+7] in sevenchar:
            shortest= min(shortest, 7)
    print(shortest if shortest != 10 else -1)



