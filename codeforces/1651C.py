import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def best_choice(nums, curr):
    best = 100000000000
    pos = -1
    for idx, num in enumerate(nums):
        if best > abs(curr - num):
            best = abs(curr - num)
            pos = idx
    return pos



for i in range(1, len(lines), 3):
    best = float("inf")
    n = int(lines[i])
    a = list(map(int, lines[i+1].split(" ")))
    b = list(map(int, lines[i+2].split(" ")))
    candidates1 = [0, best_choice(b, a[0]), n-1]
    candidates2 = [0, best_choice(b, a[n-1]), n-1]
    for var1 in candidates1:
        for var2 in candidates2:
            ans = abs(a[0] - b[var1]) + abs(a[n-1] - b[var2])
            if var1 > 0 and var2 > 0:
                ans += abs(b[0] - a[best_choice(a, b[0])])
            if var1 < n-1 and var2 < n-1:
                ans += abs(b[n-1] - a[best_choice(a, b[n-1])])
            best = min(best, ans)
    print(best)
