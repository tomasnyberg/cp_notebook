import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# Need to add more locomotives
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
    #  find such maximal index j≤k in the set, if the value a_k<a_j, then we should add the value k to the set, since it will start a new train
    # for k, diff in queries:
    #     k-=1
    #     biggest = -1
    #     add = False
    #     for j in locomotives:
    #         if k >= j and locomotives[j] > real_speeds[k]:
    #             add = True
    #             biggest = max(j, biggest)
    #     if add: locomotives[k] = real_speeds[k]
    #     to_delete = []
    #     for j in locomotives:
    #         if j >= k and real_speeds[j] > real_speeds[k]:
    #             to_delete.append(j)
    #     for td in to_delete:
    #         del locomotives[td]
    #     print(len(locomotives), end=" ")
    print(real_speeds)
    print(max_speeds)
    print(locomotives)
    print()

        

        

    print()
    i += to_skip + 3