import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    nums.sort()
    # print(nums)
    a = [1]
    if nums[0] != 1:
        print("NO")
        continue
    sub_sums = set([1])
    for i in range(1, len(nums)):
        if nums[i] not in sub_sums:
            print("NO")
            break
        a.append(nums[i])
        to_add = set()
        for sub_sum in sub_sums:
            if sub_sum + nums[i] > 5000: continue
            to_add.add(sub_sum+nums[i])
        sub_sums.update(to_add)
    else:
        print("YES")
        


