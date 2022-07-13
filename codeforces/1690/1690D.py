import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    str = lines[i+1]
    blacks = 0
    for j in range(0, k-1):
        if str[j] == 'B':
            blacks += 1
    left = 0
    right = k-1
    best = k - blacks
    while right < len(str):
        if str[right] == 'B': blacks +=1
        best = min(k-blacks, best)
        if str[left] == 'B': blacks -=1
        left += 1
        right += 1
    print(best)
