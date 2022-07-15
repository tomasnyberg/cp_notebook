import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

walls = list(map(int, lines[1].split(" ")))
sorted_walls = list(sorted(walls))
# Just take two random
best = math.ceil(sorted_walls[0]/2) + math.ceil(sorted_walls[1]/2)
# Shoot alternating
for i in range(1, len(walls)):
    a = walls[i-1]
    b = walls[i]
    shots = 0
    if a == 1 or b == 1:
        shots = 1
        a -= 1
        b -= 1
        shots += a // 2 + b // 2
        best = min(best, shots)
        continue
    if b > a:
        temp = a
        a = b
        b = temp
    alternating = b // 3
    shots = alternating * 2
    a -= (b//3)*3
    shots += math.ceil(a / 2)
    best = min(best, shots)

#Shoot at the one in the middle til two breaks
for i in range(1, len(walls) - 1):
    a = walls[i-1]
    b = walls[i+1]
    best = min(best, max(a, b))
    
print(best)