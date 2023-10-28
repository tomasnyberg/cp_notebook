import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

answer = "abc"
for line in lines[1:]:
    count = 0
    for x, y in zip(line, answer):
        if x != y:
            count += 1
    print("YES") if count < 3 else print("NO")