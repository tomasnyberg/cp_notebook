import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    line = lines[i]
    c = lines[i+1]
    found = False
    for idx, char in enumerate(line):
        if char == c and idx % 2 == 0:
            found = True
            break
    print("YES" if found else "NO")