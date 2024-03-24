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
    valid = {} # number -> idx
    moves = []
    print("Looking for index", idx)
    while True:
        if r - l == 1:
            break
        m = (l + r) // 2
        if m <= idx:
            for i in range(m):
                valid[a[i]] = i
        else:
            print("here")
            for i in range(m+1, len(a)):
                valid[a[i]] = i
        if 10**9 in valid:
            del valid[10**9]
        if m < idx and a[m] > x:
            for cand, j in valid.items():
                if cand <= x:
                    moves.append((j, m))
                    del valid[cand]
                    if j == idx:
                        idx = m
                    print("Swapping", j, m)
                    a[m], a[j] = a[j], a[m]
                    break
        if m > idx and a[m] < x:
            for cand, j in valid.items():
                if cand >= m:
                    moves.append((j, m))
                    del valid[cand]
                    if j == idx:
                        idx = m
                    print("Swapping", j, m)
                    a[m], a[j] = a[j], a[m]
                    break
        print(a[1:])
        print(m)
        print(valid)
        print()
        if a[m] <= x:
            l = m
        else:
            r = m
    # assert a[l] == x
    print(a[l], x)
    # print(moves)
    # print("\n\n")
    

        
