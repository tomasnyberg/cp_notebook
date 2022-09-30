import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def simulate(a):
    result = [0]*len(a)
    for idx, x in enumerate(a):
        added = x
        for i in range(idx, idx + len(result)):
            result[i % len(result)] += added
            added += x
    print(result)

def arithmetic_sum(a, n):
    return (n*(a+a*n))//2
# print(arithmetic_sum(6, 6))
# # simulate([5,5,4,1,4,5])
# simulate([5,5,5,5,5,5])
# print(ä)

for line in lines[2::2]:
    b = list(map(int, line.split(" ")))
    n = len(b)
    S = 2*sum(b)/(n*(n+1))
    result = [0]*n
    bad = False
    for i in range(len(b)):
        result[i] = int((S - b[i] + b[(i+n-1)%n]) // n)
        if result[i] <= 0:
            print("NO")
            bad = True
            break
    if bad: continue
    print("YES")
    print(*result)