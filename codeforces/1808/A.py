import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def score(s):
    smallest = 10
    biggest = 0
    for i in range(len(s)):
        smallest = min(smallest, int(s[i]))
        biggest = max(biggest, int(s[i]))
    return biggest - smallest

for line in lines[1:]:
    astring, bstring = map(list,line.split())
    a, b = map(int, line.split())
    best = [a, 0]
    for i in range(-100,110):
        if not a <= a+i <= b: continue
        if score(str(a+i)) > best[1]:
            best = [a+i, score(str(a+i))]
    for i in range(-100, 110):
        if not a <= b+i <= b: continue
        if score(str(b+i)) > best[1]:
            best = [b+i, score(str(b+i))]
    print(best[0])

        


