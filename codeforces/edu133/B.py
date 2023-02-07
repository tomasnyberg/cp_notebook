import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    perms = [[i+1 for i in range(n)]]
    i = 0
    for _ in range(n-1):
        copy = perms[-1][:]
        copy[i], copy[i+1] = copy[i+1], copy[i]
        perms.append(copy)
        i+=1
    print(len(perms))
    for perm in perms:
        print(*perm)