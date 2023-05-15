import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, l, r = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))[::-1]
    seen = set(nums)
    L, R = l, r
    lc, rc = {}, {}
    while l:
        popped = nums.pop()
        lc[popped] = lc.get(popped, 0) + 1
        l-=1
    while r:
        popped = nums.pop()
        rc[popped] = rc.get(popped, 0) + 1
        r-=1
    for j in seen:
        small = min(lc.get(j, 0), rc.get(j, 0))
        if j in lc:
            lc[j] -= small
        if j in rc:
            rc[j] -= small
        L -= small
        R -= small
    if L < R:
        lc, rc = rc, lc
        L, R = R, L
    result = 0
    for j in lc:
        extra = L -R
        cando = lc[j] // 2
        do = min(cando*2, extra)
        result += do // 2
        L -= do
    result += (L-R) // 2 + (L+R) // 2
    print(result)
    
