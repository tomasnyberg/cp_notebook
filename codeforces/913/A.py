import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    c, num = list(line)
    num = int(num)
    for i in range(1, 9):
        if i == num: continue
        print(c + str(i))
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        if c == col: continue
        print(col + str(num))