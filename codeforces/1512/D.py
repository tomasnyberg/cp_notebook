import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    b = list(map(int, line.split(" ")))
    total = sum(b)
    b.sort()
    # print(b)
    badindex = -1
    for candidate in b[len(b)-2:]:
        for idx, num in enumerate(b[:len(b)-2]):
            if total - num - candidate == candidate:
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