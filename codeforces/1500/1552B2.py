import sys
lines = list(map(str.strip, sys.stdin.readlines()))


i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    athletes = []
    for _ in range(n):
        athletes.append(list(map(int, lines[i].split(" "))))
        i+=1
    winner = 0
    def beats(a, b):
        return sum([1 if x < y else 0 for x, y in zip(a, b)]) >= 3
    for other in range(1, len(athletes)):
        if beats(athletes[other], athletes[winner]):
            winner = other
    if all([beats(athletes[winner], athletes[i]) for i in range(len(athletes)) if i != winner]):
        print(winner + 1)
    else:
        print(-1)
