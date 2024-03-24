import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, x = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    a = [10**9] + a
    idx = a.index(x)
    l = 1
    r = n+1
    valid = {y:i for i, y in enumerate(a)} # number -> idx
    del valid[10**9]
    # print("Looking for index", idx)
    moves = []
    while True:
        if r - l == 1:
            break
        m = (l + r) // 2
        # print("m is", m)
        greater = None
        if m < idx and a[m] > x:
            greater = False
        if m > idx and a[m] < x:
            greater = True
        if greater is not None:
            for cand, j in valid.items():
                if (greater and cand >= x) or (not greater and cand <= x):
                    moves.append((j, m))
                    # print("Swapping", j, m)
                    a[m], a[j] = a[j], a[m]
                    if a[m] in valid:
                        del valid[a[m]]
                    if a[j] in valid:
                        del valid[a[j]]
                    break
        # print(a[1:])
        # print(valid)
        # print()
        if a[m] <= x:
            l = m
        else:
            r = m
        if a[m] in valid:
            del valid[a[m]]
    # print(a[l], x)
    assert a[l] == x
    print(len(moves))
    for m in moves:
        print(m[0], m[1])
    # print(moves)
    # print("\n\n")
    

        
