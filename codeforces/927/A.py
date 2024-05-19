import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    score = 0
    for i in range(len(line)):
        if i+1 < len(line) and line[i] == '*' and line[i+1] == '*':
            break
        score += 1 if line[i] == '@' else 0
    print(score)

    