import sys
lines = list(map(str.strip, sys.stdin.readlines()))

s = "codeforces"
for line in lines[1:]:
    res = 0
    for i in range(len(line)):
        if line[i] != s[i]:
            res += 1
    print(res)