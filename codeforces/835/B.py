import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    listed = list(map(lambda x: ord(x) - 96, line))
    # print(line)
    # print(listed)

    print(max(listed))