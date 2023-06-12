import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    queries = list(map(int, line.split()))
    nums = []
    first = True
    for x in queries:
        if first:
            if not nums or x >= nums[-1]:
                nums.append(x)
            else:
                nums.append(x)
                first = False
            print("1", end="")
        else:
            if x >= nums[-1] and x <= nums[0]:
                nums.append(x)
                print("1", end="")
            else:
                print("0", end="")
    print()

