import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def comparecounts(acounts, bcounts, atotal, btotal):
    for i in range(26):
        curr = chr(i+97)


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
    acounts = {'a':1}
    bcounts = {'a':1}
    for i in range(1, 26):
        acounts[chr(i+97)] = 0
        bcounts[chr(i+97)] = 0
    atotal = 0
    btotal = 0
    for s, amount, newstr in queries:
        target_dict = acounts if s == '1' else bcounts
        amount = int(amount)
        counts = {}
        for c in newstr:
            counts[c] = 1 if c not in counts else counts[c] + 1
        for c in counts:
            target_dict[c] += counts[c] * amount 
            if s == '1':
                atotal += counts[c] * amount
            else:
                btotal += counts[c] * amount
        comparecounts(acounts, bcounts, atotal, btotal)
        print(acounts, bcounts)
    