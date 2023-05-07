import sys
lines = list(map(str.strip, sys.stdin.readlines()))
 
for line in lines[1:]:
    n, a, b = map(int, line.split(" "))
    if a == 1:
        print("YES" if (n-1) % b == 0 else "NO")
        continue
    for power in range(40):
        diff = n - pow(a, power)
        if diff % b == 0 and diff >= 0:
            print("YES")
            break
    else:
        print("NO")
 