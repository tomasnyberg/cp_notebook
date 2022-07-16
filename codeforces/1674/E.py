import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

walls = list(map(int, lines[1].split(" ")))
swalls = list(sorted(walls))

# Case 1: Shoot at two different ones far away
best = math.ceil(swalls[0]/2) + math.ceil(swalls[1]/2)

# Case 2: Two walls with one inbetween, we can always reduce them by 2 per shot.
for i in range(1, len(walls) - 1):
    left = walls[i-1]
    right = walls[i+1]
    best= min(best, math.ceil((left + right)/2))

# Case 3: Two adjacent walls
for i in range(1, len(walls)):
    x = max(walls[i-1], walls[i])
    y = min(walls[i-1], walls[i])
    if x >= y*2: # Just shoot x until it's gone, y will be destroyed in the process
        best = min(best, math.ceil(x/2))
        continue
    # Shoot x until they are equal
    shots = x - y
    x -= shots*2
    y -= shots
    # We can distribute 3 damange across x and y for every shot
    shots += math.ceil((x+y)/3)
    best = min(best, shots)

print(best)