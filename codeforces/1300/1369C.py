import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n, k = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    friends = list(map(int, lines[i+2].split(" ")))
    nums.sort()
    friends.sort()
    result = 0
    for j in range(len(friends)):
        biggest = nums.pop()
        result += biggest if friends[j] > 1 else biggest*2
        friends[j] -=1
    for j in range(len(friends)):
        last = 0
        while friends[j]:
            last = nums.pop()
            friends[j] -= 1
        if last: result+=last
    print(result)