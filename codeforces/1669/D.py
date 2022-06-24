import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# Bad case 1: B/R with white or end on both sides
# Bad case 2: Sliding window of size 3 contains all of the same color?
def solve(str):
    # check bad case 1
    for i in range(len(str)):
        if str[i] != 'W':
            left = i == 0 or str[i-1] == 'W'
            right = i == len(str) - 1 or str[i+1] == 'W'
            if left and right:
                print("NO")
                return
    #Check bad case 2
    left = 0
    right = 2
    reds = 0
    blues = 0
    for i in range(0, min(2, len(str))):
        if str[i] == 'R':
            reds += 1
        if str[i] == 'B':
            blues += 1
    while right < len(str):
        if str[right] == 'R':
            reds += 1
        if str[right] == 'B':
            blues += 1
        if reds == 3 or blues == 3:
            print("NO")
            return
        if str[left] == 'R':
            reds -= 1
        if str[left] == 'B':
            blues -= 1
        right += 1
        left += 1
    print("YES")


for i in range(2, len(lines), 2):
    str = lines[i]
    solve(str)
    # print(str)
