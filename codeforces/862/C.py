import sys
from decimal import Decimal, getcontext
import bisect

lines = list(map(str.strip, sys.stdin.readlines()))

def intersects_parabola(a, b, c, k):
    D = (b - k)**2 - 4 * a * (c)
    if D >= 0:
        return True
    else:
        return False

ii = 1
while ii< len(lines):
    n, m = map(int, lines[ii].split())
    ii+=1
    ks = []
    for _ in range(n):
        ks.append(int(lines[ii]))
        ii+=1
    parabolas = []
    for _ in range(m):
        parabolas.append(list(map(int, lines[ii].split())))
        ii+=1
    ks = list(set(ks))
    ks.sort()
    # nks = [min(ks), max(ks)]
    # for i in range(1, min(len(ks), 10)):
    #     nks.append(ks[i])
    # for i in range(len(ks)-1, max(len(ks) - 10, -1), -1):
    #     nks.append(ks[i])
    for a, b, c in parabolas:
        lb = bisect.bisect_left(ks, b)
        rb = bisect.bisect_right(ks, b)
        candidates = []
        for idx in [lb, rb]:
            if idx < len(ks):
                candidates.append(ks[idx])
            if idx > 0:
                candidates.append(ks[idx-1])
        
        for k in candidates:
            if not intersects_parabola(a, b, c, k):
                print("YES")
                print(k)
                break
        # if not intersects_parabola(a, b, c, smallestk):
        #     print("YES", a,b,c)
        #     print(smallestk)
        else:
            print("NO")
    # # print()