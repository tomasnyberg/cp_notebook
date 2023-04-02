import sys
from decimal import Decimal, getcontext

getcontext().prec = 50  # Set the precision of the decimal calculations

lines = list(map(str.strip, sys.stdin.readlines()))

def intersects_parabola(a, b, c, k):
        # Ensure the parabola is upwards open
    if a <= 0:
        raise ValueError("The parabola must be upwards open (a > 0).")

    # Find the discriminant (D) for the quadratic equation (ax^2 + bx + c - kx = 0)
    D = (b - k)**2 - 4 * a * (c)

    # Check the conditions for intersection or touching
    if D > 0:
        # The parabola and the line intersect at two distinct points
        return True
    elif D == 0:
        # The parabola and the line touch each other (tangent)
        return True
    else:
        # The parabola and the line do not intersect or touch
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