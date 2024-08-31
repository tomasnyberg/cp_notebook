import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    n = line
    remaining = n[2:]
    if len(n) >= 3 and n[:2] == '10' and remaining[0] != '0' and int(remaining) > 1:
        print("YES")
    else:
        print("NO")
