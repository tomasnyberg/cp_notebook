import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

split = lines[1].split(",")
times = []
for i in range(len(split)):
    b = split[i]
    if b != "x":
        b = int(b)
        times.append(b)
    else:
        times.append(-1)
print(times)
step = 1
n = 0
for i in range(len(times)):
    x = times[i]
    if x == -1:
        continue
    while (n + i) % x != 0:
        n += step
    step *= x
print(n)