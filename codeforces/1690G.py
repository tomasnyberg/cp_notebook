import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# Seems to work, though not 100% sure.
def slow_down_trains(trains):
    result = [trains[0]]
    locomotives = {}
    locomotive_start = -1
    for i in range(1, len(trains)):
        if result[i-1] <= trains[i]:
            result.append(result[i-1])
            if result[i-1] != locomotive_start:
                locomotives[i-1] = result[i-1]
                locomotive_start = result[i-1]
        else:
            result.append(trains[i])
    return [result, locomotives]


i = 2
while i < len(lines):
    n, k = map(int, lines[i].split(" "))
    max_speeds = list(map(int, lines[i+1].split(" ")))
    real_speeds, locomotives = slow_down_trains(max_speeds)
    queries = []
    for j in range(i+2, i+2+k):
        queries.append(list(map(int, lines[j].split(" "))))
    print(max_speeds)
    print(real_speeds)
    print(locomotives)
    print()
    i += k + 3