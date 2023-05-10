import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def count_first_char(s):
    fc = s[0]
    fc_count = 0
    for c in s:
        if c == fc:
            fc_count += 1
        else: break
    return fc_count

for i in range(1, len(lines), 2):
    a, b = lines[i], lines[i+1]
    afc, bfc = count_first_char(a), count_first_char(b)
    start = 0
    while start < len(a) and (a[start] != b[0] or (a[start] == b[0] and afc > bfc)):
        start += 1
        afc -= 1
    if start == len(a):
        print("NO")
        continue
    a = a[start:]
    dp = [0] * (len(a) + 1)
    previnc = 0
    for j in range(1, len(a) + 1):
        char = a[j-1]
        sofar = dp[j-1]
        if char == b[sofar] and (j-previnc) % 2 == 1:
            dp[j] = sofar + 1
            previnc = j
            if dp[j] == len(b):
                dp[-1] = len(b)
                break
        else:
            dp[j] = sofar
    print("YES" if dp[-1] == len(b) else "NO")

