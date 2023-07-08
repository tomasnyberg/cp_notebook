import sys
lines = list(map(str.strip, sys.stdin.readlines()))

seen = set()
def construct(k):
    total = k+1
    leaves = k
    total += leaves * k
    leaves *= k
    seen.add(total)
    for _ in range(10000):
        total += leaves * k
        seen.add(total)
        leaves *= k
        if total > 10**6:
            break

for k in range(2, 10**6):
    construct(k)

for line in lines[1:]:
    n = int(line)
    print("YES" if n in seen else "NO")
