import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    expected = [i for i in range(1, len(nums)+1)]
    result = 10**9
    g = 10**9
    for i in range(len(nums)):
        if nums[i] == expected[i]:
            continue
        expected_idx = nums[i] - 1
        away = abs(expected_idx - i)
        # print(nums[i], "Wants to be at", expected_idx, away)
        if away % g != 0:
            if g == 10**9:
                g = away
            else:
                g = gcd(g, away)
    print(g)