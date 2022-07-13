import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    chests = list(map(int, lines[i+1].split(" ")))
    sum = 0
    best = 0
    for j in range(-1, len(chests)):
        now = sum
        for g in range(j+1, min(len(chests), j+32)):
            now += chests[g] >> g -j 
        best = max(best, now)
        if j +1 != len(chests):
            sum += chests[j+1] - k
    print(best)