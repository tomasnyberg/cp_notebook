import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    a,b,l = map(int, line.split())
    result = set()
    for x in range(21):
        for y in range(21):
            if a**x * b**y > l:
                break
            if l % (a**x * b**y) == 0:
                result.add(l // (a**x * b**y))
    print(len(result))

