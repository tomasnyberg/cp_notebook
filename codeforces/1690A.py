import sys
lines = list(map(str.strip, sys.stdin.readlines()))
for line in lines[1:]:
    n = int(line)
    for i in range(0, n):
        # Should do this as binary search instead
        if i + i-1 + i-2 >= n:
            first = i
            second = i-1
            third = n - first - second
            if third == 0:
                second -= 1
                third += 1
            print(second, first, third)
            break