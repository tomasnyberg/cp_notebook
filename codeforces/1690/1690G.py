import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def slow_down_trains(trains):
    result = [trains[0]]
    for i in range(1, len(trains)):
        if result[i-1] <= trains[i]:
            result.append(result[i-1])
        else:
            result.append(trains[i])
    locomotives = {0: trains[0]}
    for i in range(1, len(result)):
        if result[i] != result[i-1]:
            locomotives[i] = result[i]
    return [result, locomotives]


i = 2
while i < len(lines):
    n, to_skip = map(int, lines[i].split(" "))
    max_speeds = list(map(int, lines[i+1].split(" ")))
    real_speeds, locomotives = slow_down_trains(max_speeds)
    queries = []
    for j in range(i+2, i+2+to_skip):
        queries.append(list(map(int, lines[j].split(" "))))
    for k, diff in queries:
        k-=1
        biggest = -1
        max_speeds[k] -= diff
        real_speeds[k] = min(max_speeds[k], real_speeds[k])
        for j in locomotives:
            if k >= j:
                biggest = max(j, biggest)
        if locomotives[biggest] > real_speeds[k]:
            locomotives[k] = real_speeds[k]
        to_delete = []
        for j in locomotives:
            if j > k and real_speeds[j] >= real_speeds[k]:
                to_delete.append(j)
        for td in to_delete:
            del locomotives[td]
        print(len(locomotives), end=" ")
    print()
    i += to_skip + 3