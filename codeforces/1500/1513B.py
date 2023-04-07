import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def nPr(n, r):
    return math.factorial(n) // math.factorial(n-r)

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))    
    # print(list(map(lambda x: bin(x)[2:], nums)))
    startvalue = 2**300-1
    for num in nums:
        startvalue &= num
    count = sum([1 if num == startvalue else 0 for num in nums])
    print(nPr(count, 2)*(math.factorial(len(nums) - 2) if len(nums) - 2 > 0 else 1)%(10**9+7) if count > 1 else 0)
