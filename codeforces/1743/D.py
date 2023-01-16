import sys
import itertools
lines = list(map(str.strip, sys.stdin.readlines()))

a = lines[1]
fills = []
for i in range(25):
    pre = a[:-i] if i > 0 else a
    pre = "0" * (len(a) - len(pre)) + pre
    assert(len(pre) == len(a))
    filled = []
    for j in range(len(pre)):
        if a[j] == '0' and pre[j] == '1':
            filled.append(j)
    if filled:
        fills.append(filled)
i = 0
while True:
    if len(fills) == 1 or all(fills[i] == fills[0] for i in range(1, len(fills))):
        break
    fills = [x for x in fills if len(x) > i]
    smallest = min(fills, key=lambda x: x[i])
    fills = [x for x in fills if x[i] == smallest[i]]
    i+=1
best = fills[0] if fills else []
a = list(a)
for i in best:
    a[i] = '1'
a = list(itertools.dropwhile(lambda x: x == '0', a))
print(''.join(a) if a != [] else '0')



