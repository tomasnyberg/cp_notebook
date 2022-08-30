import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    potentialincreases = [0]*len(line)
    result = 0
    for i in range(len(line)):
        leftscore = i
        rightscore = len(line) - i - 1
        currscore = leftscore if line[i] == 'L' else rightscore
        result += currscore
        otherscore = rightscore if line[i] == 'L' else leftscore
        if otherscore > currscore:
            potentialincreases[i] = otherscore - currscore
        else:
            potentialincreases[i] = -1
    potentialincreases.sort()
    # print(result, potentialincreases)
    for i in range(len(line)):
        popped = potentialincreases.pop()
        if popped != -1:
            result += popped
        print(result, end= " ")
    print()


