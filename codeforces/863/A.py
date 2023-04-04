import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check(s, i, d):
    scopy = s[:]
    scopy.insert(i, d)
    return ''.join(scopy)

for i in range(1, len(lines) , 2):
    n, d = map(int, lines[i].split())
    s = list(lines[i+1])
    for j in range(n):
        if d > int(s[j]):
            s.insert(j, str(d))
            break
    else:
        s.append(str(d))
    print(''.join(s))
            
    # print(greatest)
