import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, k = map(int, line.split(" "))
    low = 0
    high = 1000000000000000
    # i - i // n == k
    while low <= high:
        mid = math.floor(low + (high - low)/2)
        calc = mid - (mid // n)
        if calc == k:
            if mid % n == 0:
                mid -= 1
            print(mid)
            break
        if calc > k:
            high = mid - 1
        else:
            low = mid + 1