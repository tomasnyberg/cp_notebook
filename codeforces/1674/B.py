import sys
lines = list(map(str.strip, sys.stdin.readlines()))

indices = {}
index = 1
for i in range(97, 123):
    for j in range(97, 123):
        if i != j:
            s = chr(i) + chr(j)
            indices[s] = index
            index += 1
for line in lines[1:]:
    print(indices[line])