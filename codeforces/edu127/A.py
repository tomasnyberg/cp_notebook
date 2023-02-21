import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    # Get all the occurences of multiple as or bs
    matches = re.findall(r'(a+|b+)', line)
    for x in matches:
        if len(x) == 1:
            print("NO")
            break
    else:
        print("YES")