import sys, random
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, m = map(int, line.split(" "))
    ncopy = n
    twos = 0
    fives = 0
    while ncopy % 2 == 0:
        ncopy //= 2
        twos += 1
    ncopy = n
    while ncopy % 5 == 0:
        ncopy //= 5
        fives += 1
    multiplier = m
    for k in range(18, 0, -1):
        tn = k - twos if k-twos >= 0 else 0
        fn = k - fives if k - fives >= 0 else 0
        target = 2**tn*5**fn
        if target <= m:
            multiplier = target
            break
    result = multiplier
    for extra in range(2, 11):
        if multiplier*extra <= m:
            result = multiplier*extra
    print(n*result)
