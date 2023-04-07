import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    counts = {}
    for c in line:
        counts[c] = 1 if c not in counts else counts[c] + 1
    biggest = [-1, 'A']
    for key in counts:
        if counts[key] > biggest[0]:
            biggest = [counts[key], key]
    counters = {'R':'P', 'P':'S', 'S':'R'}
    print(counters[biggest[1]]*len(line))
        