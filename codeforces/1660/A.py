import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b = map(int, line.split(" "))
    if b == 0:
        print(a + 1)
        continue
    if a == 0:
        print(1)
        continue
    print(b*2+a+1)