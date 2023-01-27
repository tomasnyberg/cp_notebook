import sys
lines = list(map(str.strip, sys.stdin.readlines()))


pi = "3141592653589793238462643383279"
for line in lines[1:]:
    score = 0
    for i in range(min(len(pi), len(line))):
        if pi[i] == line[i]:
            score += 1
        else:
            break
    print(score)
