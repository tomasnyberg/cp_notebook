import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    result = 0
    for i in range(len(nums)-1):
        x = nums[i]
        y = nums[i+1]
        if x >= y:
            while x > (y << 1):
                # print("index", i-1, i)
                y <<= 1
                result += 1
        else:
            while y > (x << 1):
                x <<= 1
                result += 1
    print(result)