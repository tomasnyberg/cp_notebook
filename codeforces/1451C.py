import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines),3):
    n, k = map(int, lines[i].split(" "))
    a = lines[i+1]
    b = lines[i+2]
    afreq = [0]*27
    bfreq = [0]*27
    bad = False
    for j in range(len(a)):
        afreq[ord(a[j])-97] += 1
        bfreq[ord(b[j])-97] += 1
    have = 0
    for j in range(27):
        have += afreq[j]
        have -= bfreq[j]
        if have < 0 or have % k != 0:
            bad = True
            break
    if have > 0: bad = True 
    print("NO" if bad else "YES") 

    
    
