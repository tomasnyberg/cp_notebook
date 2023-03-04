import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    words = line.split()
    words.sort(key=lambda x: len(x))
    longest = max(map(len, words)) + 1
    midpoint = list(filter(lambda x: len(x) == longest // 2, words))
    if midpoint[0] == midpoint[1][::-1]:
        print("YES")
    else:
        print("NO")