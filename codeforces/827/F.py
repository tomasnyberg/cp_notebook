import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def comparecounts(acounts, bcounts, atotal, btotal):
    atotalcopy = atotal
    btotalcopy = btotal
    debuga = ""
    debugb = ""
    broken = False
    result= ""
    for i in range(26):
        curr = chr(i+97)
        atotal -= acounts[curr]
        btotal -= bcounts[curr]
        debuga += curr*acounts[curr]
        debugb += curr*bcounts[curr]
        if atotal == 0 and btotal > 0:
            result = "YES"
        if btotal == 0 and atotal > 0:
            result = "NO"
        if acounts[curr] != bcounts[curr]:
            if atotal == 0:
                if acounts[curr] < bcounts[curr]:
                    result = "YES"
                else:
                    result = "YES" if btotal > 0 else "NO"
            else:
                result = "YES" if acounts[curr] > bcounts[curr] else "NO"
    print(debuga, debugb)
    if not broken:
        print("YES" if atotalcopy < btotalcopy else "NO")
    else:
        print(result)



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
    for j in range(1, 26):
        acounts[chr(j+97)] = 0
        bcounts[chr(j+97)] = 0
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
        # print(acounts, bcounts)
    