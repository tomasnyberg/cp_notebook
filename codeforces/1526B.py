import sys
lines = list(map(str.strip, sys.stdin.readlines()))
seen = set()

for i in range(100):
    for j in range(1000):
        num = 111*i+11*j
        if num > 1099: break
        seen.add(num)


for line in lines[1:]:
    num = int(line)
    if num in seen or num > 1099:
        print("yes")
    else:
        print("no")

