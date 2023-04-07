import sys
lines = list(map(str.strip, sys.stdin.readlines()))

a = list(map(int, lines[1].split(" ")))
b = list(map(int, lines[2].split(" ")))

counts = {} # amount of left shifts -> matches if we do that
indexes = {}
for idx, x in enumerate(a):
    indexes[x] = idx
for idx, x in enumerate(b):
    otheridx = indexes[x]
    leftshifts = -1
    if idx >= otheridx:
        leftshifts = idx - otheridx
    else:
        leftshifts = idx + 1 + (len(a) - otheridx - 1)
    counts[leftshifts] = 1 if leftshifts not in counts else counts[leftshifts] + 1
print(max([counts[key] for key in counts]))