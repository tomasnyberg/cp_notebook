import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from queue import deque

nums = []
for line in lines:
    nums.append(int(line))

def part_one():
    def check(dq, target):
        for i in range(len(dq)):
            for j in range(len(dq)):
                if i != j and dq[i] + dq[j] == target:
                    return True
        return False
    dq = deque()
    for i in range(25):
        dq.append(nums[i])
    for i in range(25, len(nums)):
        if not check(dq, nums[i]):
            return nums[i]
        dq.popleft()
        dq.append(nums[i])

def part_two():
    for i in range(2, len(nums)):
        for j in range(i, len(nums)):
            curr = sum(nums[j-i:j])
            if curr == 41682220:
                return (min(nums[j-i:j]) + max(nums[j-i:j]))
        curr = nums[i-2:2]

part_one_ans = part_one()
print("Part one:", part_one_ans)
print("Part two:", part_two())
