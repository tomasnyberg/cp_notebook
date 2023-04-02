import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def intersects_parabola(a, b, c, k):
    x_vertex = -b / (2*a)
    y_vertex = a*x_vertex**2 + b*x_vertex + c
    y_line = k*x_vertex
    return y_line >= y_vertex

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
    ks = [min(ks), max(ks)]
    for a, b, c in parabolas:
        for k in ks:
            if not intersects_parabola(a, b, c, k):
                print("YES")
                print(k)
                break
        # if not intersects_parabola(a, b, c, smallestk):
        #     print("YES", a,b,c)
        #     print(smallestk)
        else:
            print("NO")
    print()