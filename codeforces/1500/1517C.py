import sys
lines = list(map(str.strip, sys.stdin.readlines()))

nums = list(map(int, lines[1].split(" ")))
result =  [[0 for _ in range(len(nums))] for _ in range(len(nums))]
for i in range(len(nums)):
    result[i][i] = nums[i]
bad = False
for i in range(len(nums)):
    remaining = result[i][i] - 1
    val = result[i][i]
    row = i
    col = i
    while remaining > 0:
        if col > 0 and result[row][col-1] == 0:
            remaining -= 1
            col -= 1
            result[row][col] = val
            continue
        if row < len(nums) - 1 and result[row+1][col] == 0:
            remaining -= 1
            row+=1
            result[row][col] = val
            continue 
        bad = True
        break
if bad:
    print(-1)
else:
    for xs in result:
        for x in xs:
            if x == 0: break
            print(x, end=" ")
        print()