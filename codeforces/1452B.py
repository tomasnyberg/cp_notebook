import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    n = len(nums)
    nums.sort()
    total = sum(nums)
    biggest = nums[-1]
    result = 0
    for i in range(len(nums)):
        if i == len(nums) - 1:
            biggest = nums[-2]
        costtomakeequal = (n-1)*biggest - (total - nums[i])
        if nums[i] <= costtomakeequal:
            result = max(result, costtomakeequal - nums[i])
            # print("here 1", result)
        else: 
            # This line is wrong
            tomakezeromod = ((nums[i]-costtomakeequal)%(n-1))
            if not tomakezeromod: continue
            result = max(result, n-1-((nums[i] - costtomakeequal)%(n-1)))
            # print("here 2", result)
    print(result)
    