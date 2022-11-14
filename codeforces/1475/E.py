import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def nCr(n,r):
    import math
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

for i in range(1, len(lines),2 ):
    n, k = map(int, lines[i].split(" "))
    bloggers = list(map(int, lines[i+1].split(" ")))
    bloggers.sort(key=lambda x: -x)
    last = bloggers[0]
    lastcount = 1
    for j in range(1, k):
        if bloggers[j] != last:
            lastcount = 1
            last = bloggers[j]
        else:
            lastcount += 1
    amount = sum(1 for x in bloggers if x == last)
    c = lastcount
    print(nCr(amount, c) % (10**9+7))