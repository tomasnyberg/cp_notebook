import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(text, stringdict):
    idx = 0
    taken = []
    while idx < len(text):
        mostprogress = [-1, ""]
        for s in stringdict:
            l = len(s)
            for j in range(l):
                if idx - j < 0:
                    break
                if idx + l > len(text):
                    continue
                if text[idx - j:idx-j+l] == s: # we can actually put in the string here
                    if l-j > mostprogress[0]:
                        mostprogress = [l-j, s]
        if mostprogress[0] == -1:
            print(-1)
            print()
            return
        print("most progress at", idx, "is equal to", mostprogress)
        idx += mostprogress[0]
    print()

i = 1
while i < len(lines):
    text = lines[i]
    i+=1
    n = int(lines[i])
    i+=1
    strings = []
    while n > 0:
        strings.append(lines[i])
        n-=1
        i+=1
    stringmap = {}
    for idx, s in enumerate(strings):
        stringmap[s] = idx + 1
    solve(text, stringmap) 