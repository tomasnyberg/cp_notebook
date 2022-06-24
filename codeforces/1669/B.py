import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n = int(lines[i])
    nums = list(map(int, lines[i+1].split(" ")))
    count = {}
    found = False
    for num in nums:
        count[num] = count[num] + 1 if num in count else 1
        if count[num] == 3:
            print(num)
            found = True
            break
    if not found:
        print(-1)