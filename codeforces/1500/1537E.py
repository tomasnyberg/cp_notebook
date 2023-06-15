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
    smallest = ""
    for i in range(len(s)):
        curr += s[i]
        extended = extend(curr, k)
        if not smallest or extended < smallest:
            smallest = extended
    print(smallest)