import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    best_unique = -1
    biggest_unique = -1
    best_started = -1
    best_ended = -1
    consecutive = {}
    for idx, num in enumerate(nums):
        if num not in consecutive:
            consecutive[num] = [0, idx]
        consecutive[num][0] += 1
        if consecutive[num][0] > biggest_unique:
            best_started = consecutive[num][1]
            best_ended = idx
            biggest_unique = consecutive[num][0]
            best_unique = num
        to_del = []
        for x in consecutive:
            if x != num:
                if consecutive[x][0] == 1:
                    to_del.append(x)
                else:
                    consecutive[x][0] -= 1
        for td in to_del:
            del consecutive[td]
    print(best_unique, best_started+1, best_ended+1)
