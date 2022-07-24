import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(name, copy_paste, queries):
    n = len(name)
    intervals = [[1, n, [1,n]]] #Start of interval, where it was copied from
    for cfrom, cto in copy_paste:
        intervals.append([intervals[-1][1]+1, intervals[-1][1] + 1 + cto - cfrom, [cfrom, cto]])
    for q in queries:
        idxofinterval = 0
        while idxofinterval < len(intervals) and q > intervals[idxofinterval][1]:
            idxofinterval += 1
        while q > len(name):
            offset = q - intervals[idxofinterval][0]
            q = intervals[idxofinterval][2][0] + offset
            while intervals[idxofinterval][0] > q:
                idxofinterval -= 1
        print(name[q-1])
i = 1
while i < len(lines):
    n, c, q = map(int, lines[i].split(" "))
    i+=1
    name = lines[i]
    i+=1
    copy_paste = []
    while c > 0:
        copy_paste.append(list(map(int, lines[i].split(" "))))
        c-=1
        i+=1
    queries = []
    while q > 0:
        queries.append(int(lines[i]))
        q-=1
        i+=1
    solve(name, copy_paste, queries)