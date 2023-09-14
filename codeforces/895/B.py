import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    traps = []
    ii += 1
    for _ in range(n):
        traps.append(list(map(int, lines[ii].split())))
        ii += 1
    earliests = {}
    for d, s in traps:
        earliests[d] = min(earliests.get(d, 100000), s+(d-1))
    def check(k):
        time = k
        for spot in range(k+1, 0, -1):
            # print(spot, time)
            if earliests.get(spot, 10**9) <= time:
                return False
            time += 1
        return True
    for k in range(1, 1000):
        # print(k, check(k))
        if not check(k):
            print(k)
            break
