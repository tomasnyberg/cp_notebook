import sys
import itertools
lines = list(map(str.strip, sys.stdin.readlines()))

a = lines
fills = []
for i in range(25):
    pre = a[:i]
    pre = "0" * (len(a) - len(pre)) + pre
    assert(len(pre) == len(a))
    filled = []
    for j in range(len(pre)):
        if a[j] == '0' and pre[j] == '1':
            filled.append(j)
    fills.append(filled)
best = min(fills)
a = list(a)
for i in best:
    a[i] = '1'
a = itertools.dropwhile(lambda x: x == '0', a)
print(''.join(a))



