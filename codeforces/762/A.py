import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    if len(line) % 2 == 1:
        print("NO")
        continue
    if line[:len(line)//2] == line[len(line)//2:]:
        print("YES")
    else:
        print("NO")