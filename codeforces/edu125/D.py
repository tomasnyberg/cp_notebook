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

increments = {}
for c, v in units:
    increments[c] = max(increments.get(c, 0), v)

dp = [0] * (C + 2)

for x in increments:
    for i in range(1, C+1):
        value = increments[x] * i
        cost = x * i
        if cost > C:
            break
        dp[cost] = max(dp[cost], value)

for i in range(1, len(dp)):
    dp[i] = max(dp[i], dp[i-1])

# print(dp)
for m in monsters:
    low = 0
    high = C + 1
    while low < high:
        mid = (low + high) // 2
        if dp[mid] > m:
            high = mid
        else:
            low = mid + 1
    print(low if low <= C else -1, end=" ")
print()


    