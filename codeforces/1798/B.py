import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    m = int(lines[i])
    i+=1
    winners = []
    n = int(lines[i])
    for _ in range(m):
        i+=1
        winners.append(list(map(int, lines[i].split())))
        i+=1
    winners = winners[::-1]
    taken = set()
    takenlist = []
    bad = False
    for j in range(len(winners)):
        bad = True
        for k in range(len(winners[j])):
            if winners[j][k] not in taken and bad:
                takenlist.append(winners[j][k])
                bad = False
            taken.add(winners[j][k])
        if bad:
            break
    if not bad:
        print(*takenlist[::-1]) 
    else:
        print(-1)