import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check_delete(xs):
    for i in range(1, len(xs)):
        if xs[i] == xs[i-1]:
            del xs[i]
            return True
    if xs[-1] == xs[0] and len(xs) > 1:
        xs.pop()
        return True
    return False

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    while check_delete(nums):
        continue
    counts = {}
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
    result = 0
    while True:
        # print(nums)
        if len(nums) == 1:
            result += 1
            break
        taken = False
        for i in range(len(nums)):
            if counts[nums[i]] > 1 and nums[i-1] != nums[(i+1)%len(nums)]:
                # print("deleteing", i)
                counts[nums[i]] -= 1
                del nums[i]
                result += 1
                taken = True
                break
        if not taken:
            counts[nums.pop()] -= 1
            # print("deleting last")
            result += 1
        while(check_delete(nums)):
            continue
    print(result)
                