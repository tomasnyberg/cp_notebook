import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    biggest = (-1, -1)
    for i in range(len(nums)):
        if nums[i] > biggest[0]:
            biggest = (nums[i], i+1)
    print(biggest[1])
    
