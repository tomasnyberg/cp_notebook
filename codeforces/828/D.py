import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


for i in range(1, len(lines), 2):
    n = int(lines[i])
    nums = list(map(int, lines[i+1].split(" ")))
    check_div_by = 2**n
    prod = 1
    for x in nums:
        prod *= x
        # this might lead to issues, but I don't think it will tbh.
        prod %= check_div_by
    if prod == 0:
        print(0)
        continue
    lowest_bit_set = -1
    for idx, x in enumerate(bin(prod)[::-1]):
        if x == '1':
            lowest_bit_set = idx
    needed = len(nums) + 1 - lowest_bit_set
    print(bin(prod), len(nums), needed)
    powsoftwo = {1 << i:i for i in range(1, 35)}
    # print(powsoftwo)
    result = 0
    for j in range(len(nums)-1,-1,-1):
        if j+1 in powsoftwo:
            needed -= powsoftwo[j+1]
            result+=1
            if needed <= 0:
                break
    if needed > 0:
        print(-1)
        continue
    print(result)
    # print(bin(prod))
    # for j in range(10,2*10**5):
    #     if j & ((1 << len(nums)) - 1) == 0:
    #         pass
    #         # print("here")