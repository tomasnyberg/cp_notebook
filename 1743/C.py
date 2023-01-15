import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    lids = list(map(int, lines[i+1]))
    nums = list(map(int, lines[i+2].split()))
    curr = []
    result = 0
    k = 0
    while k < len(lids) and lids[k] == 1:
        result += nums[k]
        k+=1
    for j in range(k, len(lids)):
        if lids[j] == 1:
            curr.append(nums[j])
        else:
            if j-1 >= 0 and lids[j-1] and curr:
                result += sum(curr) - min(curr)
            curr = [nums[j]]
    if lids[-1] and curr:
        result += sum(curr) - min(curr)
    print(result)

