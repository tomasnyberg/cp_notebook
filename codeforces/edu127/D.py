import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def merge_intervals(intervals, x):
    # Sort the intervals by their start points
    intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize the merged interval list with the first interval
    merged_intervals = [intervals[0]]

    # Merge overlapping intervals
    for interval in intervals[1:]:
        if interval[0] <= merged_intervals[-1][1]:
            # The current interval overlaps with the last merged interval,
            # so merge them by taking the maximum endpoint
            merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])]
        else:
            # The current interval does not overlap with the last merged interval,
            # so add it to the merged interval list
            merged_intervals.append(interval)

    # Remove any interval that has an endpoint greater than x
    merged_intervals = [interval for interval in merged_intervals if interval[0] <= x]

    # Truncate the last interval if its endpoint is greater than x
    if merged_intervals and merged_intervals[-1][1] > x:
        merged_intervals[-1][1] = x

    return merged_intervals


for i in range(1, len(lines), 2):
    n, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    seen = set(nums)
    xs = set([x for x in range(1, x+1) if x not in seen])
    indices = {}
    for j in range(n):
        if nums[j] not in indices:
            indices[nums[j]] = []
        indices[nums[j]].append(j)
    total = 0
    intervals = []
    for j in range(1, n):
        total += abs(nums[j] - nums[j-1])
        intervals.append([min(nums[j], nums[j-1]), max(nums[j], nums[j-1])])
    intervals = merge_intervals(intervals, x) if intervals else []
    for interval in intervals:
        for num in range(interval[0], interval[1] + 1):
            if num in xs:
                xs.remove(num)
    if not xs:
        print(total)
        continue
    xs = sorted(list(xs))
    big = xs[-1]
    small = xs[0]
    for j in range(1, len(xs)):
        total += abs(xs[j] - xs[j-1])
    start = min(abs(small - nums[0]), abs(big - nums[0]))
    end = min(abs(small - nums[-1]), abs(big - nums[-1]))
    min_to_add = [min(start, end), 0]
    for j in range(1, len(nums) - 1):
        increasing_before = abs(small - nums[j-1]) + abs(big - nums[j]) - abs(nums[j] - nums[j-1])
        increasing_after = abs(small - nums[j]) + abs(big - nums[j+1]) - abs(nums[j] - nums[j+1])
        decreasing_before = abs(big - nums[j-1]) + abs(small - nums[j]) - abs(nums[j] - nums[j-1])
        decreasing_after = abs(big - nums[j]) + abs(small - nums[j+1]) - abs(nums[j] - nums[j+1])
        smallest = min(increasing_before, increasing_after, decreasing_before, decreasing_after)
        if smallest < min_to_add[0]:
            min_to_add = [smallest, j]
    total += min_to_add[0]
    # print(xs)
    # print(min_to_add)
    # print()
    print(total)
    