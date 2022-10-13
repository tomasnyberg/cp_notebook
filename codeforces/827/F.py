import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def comparecounts(acounts, bcounts, amax, bmax):
    debuga = ""
    debugb = ""
    atotal = 0
    btotal = 0
    result = "NO"
    canmatch = True
    for i in range(25, -1,-1):
        debuga += chr(i+97)*acounts[i]
        debugb += chr(i+97)*bcounts[i]
        if btotal > atotal:
            result = "YES"
            break
        atotal += acounts[i]
        btotal += bcounts[i]
    if btotal > atotal:
        result = "YES"
    print(debuga, debugb)
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
    acounts = [1] + [0]*25
    bcounts = [1] + [0]*25
    atotal = 1
    btotal = 1
    for s, amount, newstr in queries:
        target_dict = acounts if s == '1' else bcounts
        amount = int(amount)
        counts = {}
        for c in newstr:
            counts[c] = 1 if c not in counts else counts[c] + 1
        for c in counts:
            target_dict[ord(c)-97] += counts[c] * amount 
            if s == '1':
                atotal += counts[c] * amount
            else:
                btotal += counts[c] * amount
        comparecounts(acounts, bcounts, atotal, btotal)
        # print(acounts, bcounts)
    