import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def binary_search(target):
    low = 1
    high = 10010
    while low < high:
        mid = (low+high) >> 1
        res = mid**3
        if res == target: return res
        if res < target:
            low = mid + 1
        else:
            high = mid
    return low**3

for line in lines[1:]:
    num = int(line)
    good = False
    for i in range(1, min(10000, num)):
        a = i**3
        other = binary_search(num - a)
        if a + other == num:
            good = True
            break
    print("YES" if good else "NO")
