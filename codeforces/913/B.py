import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    removed = set()
    small = []
    big = []
    result = []
    j = 0
    for i, c in enumerate(line):
        if c == 'b':
            if small:
                removed.add(small.pop())
        elif c == 'B':
            if big:
                removed.add(big.pop())
        else:
            if c.isupper():
                big.append(j)
            else:
                small.append(j)
            result.append(c)
            j+=1
    print(''.join([c for i, c in enumerate(result) if i not in removed]))
        