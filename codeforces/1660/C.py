import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    prev = [False]*26
    m = 0
    for c in line:
        if prev[ord(c) -97]:
            m += 2
            prev = [False]*26
        else:
            prev[ord(c) - 97] = True
    print(len(line) - m)
            

