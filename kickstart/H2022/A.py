import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
test = 1
while i < len(lines):
    L, N = map(int, lines[i].split(" "))
    i+=1
    nums = []
    dirs = []
    for _ in range(N):
        split = lines[i].split(" ")
        nums.append(int(split[0]))
        dirs.append(split[1])
        i+=1
    result = 0
    dir = 0 # 0 = clockwise 1 = counter clockwise
    pos = 0
    for j in range(N):
        if dirs[j] == 'C':
            pos += nums[j]
            if pos >= 0:
                result += pos // L
                pos %= L
        else:
            pos -= nums[j]
            if pos <= 0:
                result += (-pos)//L
                pos = -pos
                pos %= L
                pos = -pos




    print(f"Case #{test}: {result}")
    test += 1
    # print(nums, dirs)