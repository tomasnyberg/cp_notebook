import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    counts = [0]*(n+1)
    for num in nums:
        counts[num] += 1
    if nums[0] == nums[-1]:
        print("YES" if counts[nums[0]] >= k else "NO")
    else:
        first_count = 0
        last_count = 0
        for x in nums:
            if x == nums[0]:
                first_count += 1
            if x == nums[-1]:
                if first_count >= k:
                    last_count += 1
        print("YES" if last_count >= k else "NO")