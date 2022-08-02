import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, H, M = map(int, lines[i].split(" "))
    x = H*60 + M
    i+=1
    mindiff = 10000000000
    while n > 0:
        hour, minute = map(int, lines[i].split(" "))
        y = hour * 60 + minute
        diff = y - x
        if diff < 0:
            diff += 1440
        i+=1
        n-=1
        mindiff = min(mindiff,diff)
    print(mindiff//60, mindiff%60)