import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# think this is correct
def operation(xs, l, r):
    pre = xs[:l]
    mid = xs[l:r+1]
    post = xs[r+1:]
    return post + mid[::-1] + pre

# If largest is not first, then it should be 

for line in lines[2::2]:
    p = list(map(int, line.split(" ")))
    if len(p) == 1:
        print(1)
        continue
    # if p[0] == len(p):
    #     # TODO
    #     print("NOT DONE")
    #     # start = p.index(len(p)-1)-1¨'
    #     continue
    candidates = []
    if p[-1] == len(p) or (p[0] == len(p) and p[-1] == len(p) - 1):
        candidates.append([p[-1]] + p[:-1])
    start = p.index(len(p)) - 1 if p[0] != len(p) else p.index(len(p)-1) - 1
    for l in range(start, -1, -1):
        candidates.append(operation(p, l, start))
    print(*max(candidates))

