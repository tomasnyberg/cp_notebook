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
    x = max(a,b)
    y = min(a,b)
    if x >= 2*y:
        best = min(best, math.ceil(x/2))
        continue
    shots = x-y
    x -= shots*2
    y -= shots
    shots += math.ceil((x+y)/3)
    best = min(shots, best)

#Two apart by one
for i in range(1, len(walls) - 1):
    a = walls[i-1]
    b = walls[i+1]
    best = min(best, math.ceil((a+b)/2))
    
print(best)