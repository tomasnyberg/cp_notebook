import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n = int(lines[i])
    nums = list(map(int, lines[i+1].split(" ")))
    evens_even = True
    evens_odd = True
    odds_odd = True
    odds_even = True
    for j in range(len(nums)):
        if j % 2 == 0:
            if nums[j] % 2 != 0: evens_even = False
            if nums[j] % 2 != 1: evens_odd = False
        if j % 2 == 1:
            if nums[j] % 2 != 0: odds_even = False
            if nums[j] % 2 != 1: odds_odd = False
    if (evens_even and (odds_odd or odds_even)) or (evens_odd and (odds_odd or odds_even)):
        print("YES")
    else:
        print("NO")
