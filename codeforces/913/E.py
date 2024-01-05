import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    n = int(line)
    cnt = 1
    while n > 0:
        d = n % 10
        n //= 10
        if d == 0:
            continue
        mul = 0
        for i in range(d+1):
            for j in range(d+1):
                if d-i-j >= 0:
                    mul += 1
        # print(d, n, "mul", mul)
        cnt *= mul
    print(cnt)


# 12
# 11 9
# 0 1
# 1 3
# 2 6
# 3 10
# 4 15
# 5 21
# 3141 1350
# 999 166375
# 2718 29160
# 9999999 1522435234375
# 10000000 3
