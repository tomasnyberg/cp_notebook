import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    line = list(line)
    if n % 7 == 0:
        print(n)
        continue
    for i in range(0, 10):
        line[-1] = str(i)
        joined = int(''.join(line))
        if joined % 7 == 0 and joined != 0:
            print(joined)
            break

