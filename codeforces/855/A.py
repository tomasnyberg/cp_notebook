import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    s = line.lower()
    index = 0
    meow = "meow"
    seenw = False
    for c in s:
        if c == meow[index]:
            continue
        elif index < 3 and c == meow[index+1]:
            index += 1
            if index == 3:
                seenw = True
        else:
            seenw = False
            break
    if index == 3 and seenw:
        print("YES")
    else:
        print("NO")
