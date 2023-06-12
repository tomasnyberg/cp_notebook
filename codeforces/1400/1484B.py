import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
# for line in ["1 3 5 7 9 0 2 4 6"]:
    nums = list(map(int, line.split()))
    positives = set()
    negatives = set()
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] >= 0:
            positives.add(nums[i+1] - nums[i])
        else:
            negatives.add(nums[i] - nums[i+1])
    if len(positives) > 1 or len(negatives) > 1:
        print(-1)
        continue
    if len(positives) == 0 or len(negatives) == 0:
        print(0)
        continue
    a = positives.pop() 
    b = negatives.pop()
    m = a + b
    c = a
    if any([x >= m for x in nums]):
        print(-1)
        continue
    print(m, c)
        





