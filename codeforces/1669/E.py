import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    strs = []
    while n > 0:
        strs.append(lines[i])
        i += 1
        n-=1
    counts = {}
    result = 0
    for str in strs:
        if str in counts:
            result += counts[str]
            print("matches for", str, counts[str])
        c = str[0]
        charc = ord(str[0])
        for j in range(97, 123):
            if j != charc:
                counts[c + chr(j)] = counts[c + chr(j)] + 1 if c + chr(j) in counts else 1
        c = str[1]
        charc = ord(str[1])
        for j in range(97, 123):
            if j != charc:
                counts[chr(j) + c] = counts[chr(j) + c] + 1 if chr(j) + c in counts else 1
    
    print(counts)
    print()
    # print(result)
    print(strs)
    break
