import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, s1, s2 = map(int, lines[i].split())
    nums = list(map(int, lines[i+1].split()))
    for j in range(len(nums)):
        nums[j] = (j+1, nums[j])
    nums.sort(key=lambda x: x[1])
    a = []
    b = []
    acost = s1
    bcost = s2
    while nums:
        elem, amount = nums.pop()
        atotal = acost * amount
        btotal = bcost * amount
        if atotal < btotal:
            a.append(elem)
            acost += s1
        else:
            b.append(elem)
            bcost += s2
    print(len(a), *a)
    print(len(b), *b)