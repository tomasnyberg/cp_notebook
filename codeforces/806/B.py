import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    seen = set()
    result = 0
    for c in line:
        if c in seen:
            result +=1
        else:
            result += 2
        seen.add(c)
    print(result)