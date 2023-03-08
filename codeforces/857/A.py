import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    reversed = nums[:]
    reversed.sort(reverse=True)
    nums.sort()
    score = 0
    for x in reversed:
        if x > 0:
            score += 1
        else:
            score -= 1
        print(score, end=" ")
    print()
    negatives = sum(1 for x in nums if x < 0)
    for _ in range(negatives):
        print("1", end=" ")
        print("0", end=" ")
    score = 0
    for _ in range(len(nums) - negatives*2):
        score += 1
        print(score, end=" ")
    print()