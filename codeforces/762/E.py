import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    nums.sort()
    seen = set([nums[0]])
    counts = {}
    for num in nums:
        counts[num] = 1 if num not in counts else counts[num] + 1
    # Take care of 0
    dp = [0]
    print(counts[0], end=" ")
    bad = False
    stack = []
    i = 1
    for i in range(1, len(nums)+ 1):
        if bad:
            print(-1, end=" ")
            continue
        if i-1 in seen or i-1 in counts:
            dp.append(dp[i-1])
        else:
            if not stack:
                bad = True
                print(-1, end=" ")
                continue
            # print()
            # print(stack, seen)
            biggest = stack.pop()
            seen.add(i-1)
            # Add however much we need to create i-1 (i-1-biggest) + however much we need to create all nums up to
            # and including i-1
            # I think this part works assuming our stack is always correct, worked with the heapq solut
            dp.append((i-1) - biggest + dp[i-1])
        print((counts[i] if i in counts else 0) + dp[i], end=" ")
        if i < len(nums) and nums[i] in seen:
            stack.append(nums[i])
        if i < len(nums): seen.add(nums[i])
    print()
    # print(dp)

