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
    def beats(a, b):
        return sum([1 if x < y else 0 for x, y in zip(a, b)]) >= 3
    candidates = set([i for i in range(len(athletes))])
    result = -1
    while candidates:
        candidate = candidates.pop()
        to_remove = set()
        beatcount = 0
        for other in range(len(athletes)):
            if beats(athletes[candidate], athletes[other]):
                beatcount += 1
                to_remove.add(other)
        candidates -= to_remove
        if beatcount == len(athletes) - 1:
            result = candidate + 1
            break
    print(result)