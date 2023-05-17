import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    if len(line) <= 3:
        print("NO")
        continue
    for i in range(len(line) // 2 - 1):
        if line[i] != line[i+1]:
            print("YES")
            break
    else:
        print("NO")