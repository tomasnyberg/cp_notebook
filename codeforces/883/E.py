import sys
lines = list(map(str.strip, sys.stdin.readlines()))

seen = set()
def construct(k):
    total = k+1
    leaves = k
    total += leaves * k
    leaves *= k
    if total > 10**18:
        return
    seen.add(total)
    for _ in range(10000):
        total += leaves * k
        leaves *= k
        if total > 10**18:
            break
        seen.add(total)

for k in range(2, 10**7):
    construct(k)
print(len(seen))

for line in lines[1:]:
    n = int(line)
    print("YES" if n in seen else "NO")
