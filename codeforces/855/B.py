import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split())
    s = lines[i + 1]
    count_lower = [0]*26
    count_upper = [0]*26
    for c in s:
        if c.islower():
            count_lower[ord(c) - ord('a')] += 1
        else:
            count_upper[ord(c) - ord('A')] += 1
    result = 0
    for j in range(26):
        small = min(count_lower[j], count_upper[j])
        big = max(count_lower[j], count_upper[j])
        while k > 0 and big - small > 1:
            small += 1
            big -= 1
            k -= 1
        result += min(small, big)
    print(result)
    # print(s)
    # print(count_lower)
    # print(count_upper)
    # print()