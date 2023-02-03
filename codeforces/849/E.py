import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    smallestmagnitude = 10**9
    for num in nums:
        if abs(num) < smallestmagnitude:
            smallestmagnitude = abs(num) 
    negatives = [num for num in nums if num < 0]
    if len(negatives) % 2 == 0:
        print(sum(abs(num) for num in nums))
    else:
        print(sum(abs(num) for num in nums) - 2*smallestmagnitude)
