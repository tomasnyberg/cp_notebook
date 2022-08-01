import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# [1,2, 4, 8, 16 ,22 ,24 ,28 ,36 ,42, 44, 48, 56] Case 1
# [5, 10] Case X 
# [11, 12, 14, 18, 26, 32, 34, 38, 46, 52, 54, 58] Case 2

def fivecheck(nums):
    for i in range(len(nums)):
        if not (nums[i]%5 == 0 or nums[i]%10 ==0):
            print("NO")
            return
        nums[i] += nums[i] % 10
    first = nums[0]
    for x in nums:
        if x != first:
            print("NO")
            return
    print("YES")

# fivecheck([10, 5, 5, 5, 5, 10, 20, 25, 0, 8])
# fivecheck([10, 5, 5, 5, 5, 10])
# fivecheck([5,5,5,5,5,5,5])

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    fivefound = False
    for x in nums:
        if x % 5 == 0 or x % 10 == 0:
            fivefound = True
            break
    if fivefound:
        fivecheck(nums)
        continue
    for i in range(len(nums)):
        if nums[i] < 10:
            mod10 = nums[i] % 10
            if mod10 == 1 or mod10 == 2 or mod10 == 4 or mod10 == 8:
                nums[i] = 1
            else:
                nums[i] = 2
        else:
            mod10 = nums[i] % 10
            if mod10 == 1 or mod10 == 2 or mod10 == 4 or mod10 == 8:
                if int(str(nums[i])[-2]) % 2 == 0:
                    nums[i] = 1
                else:
                    nums[i] = 2
            else:
                if int(str(nums[i])[-2]) % 2 == 0:
                    nums[i] = 2
                else:
                    nums[i] = 1
    first = nums[0]
    good = True
    for x in nums:
        if x != first:
            good = False
            break
    print("YES" if good else "NO")
