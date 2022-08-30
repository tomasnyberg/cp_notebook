import sys
lines = list(map(str.strip, sys.stdin.readlines()))

expected = list("Timur")
expected.sort()
# print(expected)

for line in lines[2::2]:
    listed = list(line)
    listed.sort()
    print("YES" if listed == expected else "NO")