import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# def solve(low, high):


for i in range(1, len(lines), 2):
    l, r, x = map(int, lines[i].split(" "))
    a, b = map(int, lines[i+1].split(" "))
    # Always change the low to the high
    low = min(a,b)
    high = max(a,b)
    if high == low:
        print(0)
        continue
    if (high + x > r and high - x < l) or (low + x > r and low - x < l):
        print(-1)
        continue
    if abs(high - low) >= x:
        print(1)
        continue
    if (high - l >= x and low - l >= x) or (r - low >= x and r - high >= x):
        print(2)
    else:
        print(3)
    # print("dunno")