from random import getrandbits
import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


RANDOM = getrandbits(32)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


for ii in range(1, len(lines), 5):
    a = list(map(int, lines[ii+1].split()))
    b = list(map(int, lines[ii+2].split()))
    ds = list(map(int, lines[ii+4].split()))
    for xs in [a, b, ds]:
        for i, x in enumerate(xs):
            xs[i] = Wrapper(x)
    bset = set(b)
    needed = {}
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            if y not in needed:
                needed[y] = []
            needed[y].append(i)
    bad = 0
    for x in ds:
        if x in needed:
            a[needed[x].pop()] = x
            if not needed[x]:
                del needed[x]
            bad = 0
        elif x in bset:
            bad = 0
        else:
            if not needed:
                bad += 1
    print("YES" if not needed and bad == 0 else "NO")
