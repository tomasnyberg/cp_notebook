import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    s = line
    if len(s) % 2 == 1:
        print(-1)
        continue
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    # print(counts)
    if any(val > len(s) // 2 for val in counts.values()):
        print(-1)
        continue
    conflicts = {}
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - i - 1]:
            conflicts[s[i]] = conflicts.get(s[i], 0) + 1
    # print(conflicts)
    conflicts = [v for v in conflicts.values()]
    m = max(conflicts) if conflicts else 0
    k = sum(conflicts)
    print(max(m, (k+1)//2))
    continue
    result = 0
    curr = 0
    while conflicts:
        curr = conflicts.pop()
        if not curr: continue
        while curr and conflicts:
            if curr <= conflicts[-1]:
                result += curr
                conflicts[-1] -= curr
                curr = 0
                break
            else:
                take = conflicts.pop()
                result += take
                curr -= take
    result += curr
    print(result)


