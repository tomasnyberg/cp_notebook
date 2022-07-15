import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    s = lines[i]
    t = lines[i+1]
    if t == 'a':
        print(1)
        continue
    if 'a' in t:
        print(-1)
        continue
    print(2**len(s))
    