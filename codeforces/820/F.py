import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def subsums(s, w):
    left = 0
    right = 0
    curr = ""
    result = []
    while right < len(s):
        curr += s[right]
        if len(curr) == w:
            result.append((int(curr), left+1))
            curr = curr[1:]
            left += 1
        right += 1
    result.sort()
    return result

i = 1
while i < len(lines):
    s = lines[i]
    w, m = map(int, lines[i+1].split(" "))
    i+=2
    queries = []
    while m > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        m-=1
        i+=1
    substringsums = subsums(s, w)
    for l, r, k in queries:
        print(l, r, k)

