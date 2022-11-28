import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from queue import deque

nums = []
for line in lines:
    nums.append(int(line))
    
def check(dq, target):
    for i in range(len(dq)):
        for j in range(len(dq)):
            if i != j and dq[i] + dq[j] == target:
                return True
    return False

dq = deque()
for i in range(25):
    dq.append(nums[i])
result = 0
for i in range(25, len(nums)):
    if not check(dq, nums[i]):
        print(nums[i])
        break
        result += 1
    dq.popleft()
    dq.append(nums[i])

broken = False
for i in range(2, len(nums)):
    if broken: break
    for j in range(i, len(nums)):
        curr = sum(nums[j-i:j])
        if curr == 41682220:
            print(min(nums[j-i:j]) + max(nums[j-i:j]))
            broken = True
            break
    curr = nums[i-2:2]
