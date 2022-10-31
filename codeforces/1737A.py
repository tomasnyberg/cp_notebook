import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def MEX(arr):
    s = set(arr)
    for i in range(27):
        if i not in s: return i

for i in range(1, len(lines),2):
    n, k = map(int, lines[i].split(" "))
    s = lines[i+1]
    counts = {}
    for c in s:
        orded = ord(c)
        counts[orded] = 1 if orded not in counts else counts[orded] + 1
    mexes = [97]*(k)
    put_in = [0]*(k)
    for j in range(len(mexes)):
        for c in range(97, 122):
            if put_in[j] == (n//k): continue
            # Because then we cannot increase the mex
            if c not in counts or counts[c] == 0:
                # print("breaking at", chr(c), "for index", j)
                break
            mexes[j] += 1
            counts[c] -= 1
            put_in[j] += 1
    print(''.join(list(map(chr, mexes))))
    