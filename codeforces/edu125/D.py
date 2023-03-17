import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, C = map(int, lines[0].split())
i = 1
units = []
monsters = []
for _ in range(n):
    unit = (list(map(int, lines[i].split())))
    units.append((unit[0], unit[1] * unit[2])) 
    i+=1
m = int(lines[i])
i+=1
for _ in range(m):
    monster = (list(map(int, lines[i].split())))
    monsters.append(monster[0] * monster[1]) 
    i+=1

for m in monsters:
    low = 0
    high = C + 1
    while low < high:
        mid = (low + high) // 2
        for u in units:
            count = mid // u[0]
            if count * u[1] > m:
                high = mid
                break
        else:
            low = mid + 1
    print(low if low != C + 1 else -1, end=" ")
print()


    