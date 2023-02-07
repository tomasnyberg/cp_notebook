import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    mod = n % 3
    if n == 1:
        print(2)
    elif n == 4:
        print(2)
    elif mod == 0:
        print(n//3)
    else:
        print(n// 3 + 1)
        