import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines),3):
    n, k = map(int, lines[i].split(" "))
    a = lines[i+1]
    b = lines[i+2]
    have = [0]*27
    need = [0]*27
    for j in range(n):
        have[ord(a[j]) - 97] += 1
        need[ord(b[j]) - 97] += 1
    print(have)
    print(need)
    bad = False
    for j in range(25, -1, -1):
        have[j]+=have[j+1]
        need[j] += need[j+1]
        if have[j] > need[j] or (need[j] - have[j]) % k != 0:
            bad = True
            break
    print("NO" if bad else "YES") 

    
    
