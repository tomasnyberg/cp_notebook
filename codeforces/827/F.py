import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def comparecounts(acounts, bcounts, amax, bmax):
    if bmax > 0 or (amax == bmax and acounts[amax] < bcounts[bmax]):
        print("YES")
    else:
        print("NO")

i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    queries = []
    while n > 0:
        d, k, x = lines[i].split(" ")
        queries.append((d,k,x))
        i += 1
        n -= 1
    acounts = [1] + [0]*25
    bcounts = [1] + [0]*25
    amax = 0
    bmax = 0
    for s, amount, newstr in queries:
        target_counts = acounts if s == '1' else bcounts
        amount = int(amount)
        counts = {}
        for c in newstr:
            counts[c] = 1 if c not in counts else counts[c] + 1
        for c in counts:
            target_counts[ord(c)-97] += counts[c] * amount 
            if s == '1': amax = max(amax, ord(c)-97)
            else: bmax = max(bmax, ord(c)-97)
        comparecounts(acounts, bcounts, amax, bmax)
    