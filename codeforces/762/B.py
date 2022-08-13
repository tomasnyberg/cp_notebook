import sys, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

good = []
seen = set()

for i in range(1, 2*10**5):
    if i**2 > 10**9: break
    if i**2 not in seen:
        good.append(i**2)
        seen.add(i**2)
    if i**3 not in seen:
        good.append(i**3)
        seen.add(i**3)
good.sort()
for line in lines[1:]:
    n = int(line)
    print(bisect.bisect(good, n))
