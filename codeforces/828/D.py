import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n = int(lines[i])
    nums = list(map(int, lines[i+1].split(" ")))
    s = 0
    ops = []
    for j in range(1, len((nums))+1):
        x = nums[j-1]
        while x % 2 == 0:
            s+=1
            x //= 2
        cur = j
        val = 0
        while cur % 2 == 0:
            # print("HERE")
            cur //= 2
            val += 1
        ops.append(val)
    ops.sort()
    ops.reverse()
    if s >= n:
        print(0)
        continue
    found = False
    for j in range(len(ops)):
        s += ops[j]
        if s >= n:
            found = True
            print(j+1)
            break
    if not found:
        print(-1)
        