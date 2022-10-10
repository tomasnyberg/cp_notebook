import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines),2 ):
    a, b = map(int, lines[i].split(" "))
    s = lines[i+1]
    ones = 0
    zeros = 0
    for c in s:
        if c == '1': ones += 1
        if c == '0': zeros += 1
    zerostoputin = a - zeros
    onestoputin = b - ones
    if zerostoputin < 0 or onestoputin < 0:
        print(-1)
        continue
    s = list(s)
    for idx, c in enumerate(s):
        if c != '?': continue
        otherend = s[len(s)-idx-1] 
        if otherend == '?': continue
        if otherend == '1':
            s[idx] = '1'
            onestoputin -= 1
        else:
            s[idx] = '0'
            zerostoputin -= 1
    for idx, c in enumerate(s):
        if c != '?': continue
        # print(s, idx)
        assert('?' == s[len(s)-idx-1])
        if onestoputin <= zerostoputin:
            s[idx] = '0'
            s[len(s) -idx-1] = '0'
            zerostoputin -= 2
            if idx == len(s) - idx - 1: zerostoputin += 1
        else:
            s[idx] = '1'
            s[len(s) -idx-1] = '1'
            onestoputin -= 2
            if idx == len(s) - idx - 1: onestoputin += 1
    if zerostoputin == 0 and onestoputin == 0 and s == s[::-1]:
        print(''.join(s))
    else:
        print(-1)

