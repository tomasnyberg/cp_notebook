import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    counts = {}
    doubles = 0
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
        if counts[x] == 2:
            doubles += 1
    left = doubles
    right = doubles
    used = doubles*2
    for key in counts:
        if counts[key] == 1:
            if left > right:
                right +=1
            else:
                left += 1
            used += 1
    print(max(left, right))