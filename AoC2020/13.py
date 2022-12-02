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

def part_one():
    num = int(lines[0])
    smallest = [10**9, -1]
    for i in range(len(times)):
        if times[i] == -1:
            continue
        wait = (math.ceil(num / times[i]) * times[i]) - num
        if wait < smallest[0]:
            smallest = [wait, times[i]]
    return smallest[0] * smallest[1]

def part_two():
    step = 1
    n = 0
    for i in range(len(times)):
        x = times[i]
        if x == -1:
            continue
        while (n + i) % x != 0:
            n += step
        step *= x
    return n

print("Part one:", part_one())
print("Part two:", part_two())
