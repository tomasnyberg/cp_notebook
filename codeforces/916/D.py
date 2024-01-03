import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 4):
    a = list(enumerate(map(int, lines[ii+1].split())))
    b = list(enumerate(map(int, lines[ii+2].split())))
    c = list(enumerate(map(int, lines[ii+3].split())))
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    c.sort(key=lambda x: x[1])
    a = a[-3:]
    b = b[-3:]
    c = c[-3:]
    result = 0
    for i, x in a:
        for j, y in b:
            for k, z in c:
                if i != j and j != k and i != k:
                    result = max(result, x+y+z)
    print(result)
