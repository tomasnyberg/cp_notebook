import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    result = [0]
    positions = {}
    sorted_nums = list(sorted(nums))
    # print(nums, sorted_nums)
    for i, x in enumerate(nums):
        if x not in positions:
            positions[x] = [[], []]
        positions[x][i % 2].append(i)
    for i, x in enumerate(sorted_nums):
        if not positions[x][i % 2]:
            print("NO")
            break
        positions[x][i % 2].pop()
    else:
        print("YES")
