import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 4):
    awords = lines[i+1].split(" ")
    bwords = lines[i+2].split(" ")
    cwords = lines[i+3].split(" ")
    counts = {}
    for arr in [awords, bwords, cwords]:
        for word in arr:
            counts[word] = 1 if word not in counts else counts[word] + 1
    for arr in [awords, bwords, cwords]:
        score = 0
        for word in arr:
            if counts[word] == 1: score+=3
            elif counts[word] == 2: score +=1
        print(score, end=" ")
    print()
