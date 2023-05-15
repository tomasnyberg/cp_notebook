import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n = int(lines[0])
s = "codeforces"
counts = [1]*len(s)
mult = 1
i = 0
while mult < n:
    mult //= counts[i]
    counts[i] += 1
    mult *= counts[i]
    i = (i+1) % len(s)
result = ""
for i in range(len(s)):
    result += s[i]*counts[i]
print(result)

        