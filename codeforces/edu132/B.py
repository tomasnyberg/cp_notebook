import sys
lines = list(map(str.strip, sys.stdin.readlines()))

n, m = map(int, lines[0].split())
nums = list(map(int, lines[1].split()))
CS_left = [0]
CS_right = [0]
total = 0
for i in range(1,n):
    if nums[i] < nums[i-1]:
        total += nums[i-1] - nums[i]
    CS_left.append(total)

total = 0
for i in range(n-2, -1, -1):
    if nums[i] < nums[i+1]:
        total += nums[i+1] - nums[i]
    CS_right.append(total)
CS_right.reverse()
for i in range(m):
    s, e = map(int, lines[i+2].split())
    if s == e:
        print(0)
    elif s < e:
        print(CS_left[e-1] - CS_left[s-1])
    else:
        print(CS_right[e-1] - CS_right[s-1])
