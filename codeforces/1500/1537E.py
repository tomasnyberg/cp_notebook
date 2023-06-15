import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def extend(s, k):
    result = s
    idx = 0
    while len(result) < k:
        result += s[idx]
        idx += 1
        idx %= len(s)
    return result

ii = 0
while ii < len(lines):
    n, k = map(int, lines[ii].split())
    s = lines[ii+1]
    ii += 2
    s = list(s)
    prefixes = []
    curr = ""
    for i in range(len(s)):
        curr += s[i]
        prefixes.append(extend(curr, k))
    prefixes.sort()
    best = prefixes[0]
    while len(best) < k:
        best += best
    print(best[:k])