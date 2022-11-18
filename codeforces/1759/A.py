import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    if line[0] not in ['Y', 'e', 's']:
        print("NO")
        continue
    idx = -1
    expect = "Yes"
    if line[0] == 'Y':
        idx = 1
    if line[0] == 'e':
        idx = 2
    if line[0] == 's':
        idx = 0
    bad = False
    for c in line[1:]:
        if c != expect[idx]:
            bad = True
            break 
        idx+=1
        idx %= 3
    print("NO" if bad else "YES")