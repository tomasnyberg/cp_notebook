import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    if line.lower() == "yes":
        print("YES")
    else:
        print("NO")
