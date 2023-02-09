import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    prod = 1
    cum_prod = []
    for num in nums:
        prod *= num
        cum_prod.append(prod)
    for k in range(len(nums)):
        if cum_prod[k]**2 == cum_prod[-1]:
            print(k+1)
            break
    else:
        print(-1)

