import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    b = list(map(int, line.split(" ")))
    total = sum(b)
    b.sort()
    badindex = -1
    for i in range(len(b)-1,len(b)-3, -1):
        candidate = b[i]
        for idx, num in enumerate(b):
            if total - num - candidate == candidate and idx != i:
                badindex = idx
                break
        if badindex != -1:
            break
    if badindex == -1:
        print(-1)
        continue
    del b[badindex]
    b.pop()
    print(*b)