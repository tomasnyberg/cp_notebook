import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    seen = set()
    i = 0
    result = 1
    while i < len(line):
        curr = line[i]
        if line[i] in seen:
            i += 1
        else:
            if len(seen) < 3:
                seen.add(curr)
                i+=1
            else:
                result += 1
                seen.clear()
                seen.add(curr)
                i+=1
    print(result)