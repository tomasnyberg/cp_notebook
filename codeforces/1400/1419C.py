import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    if all([y == x for y in nums]):
        print(0)
        continue
    if sum([y - x for y in nums]) == 0 or any([y == x for y in nums]):
        print(1)
        continue
    print(2)