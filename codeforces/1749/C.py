import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def play(nums, k):
    removed = set()
    def alice(nums, i):
        candidate = None
        for idx, x in enumerate(nums):
            if idx in removed: continue
            if x <= k - i + 1:
                if not candidate or x > candidate[0]:
                    candidate = (x, idx) 
        if not candidate:
            return False
        removed.add(candidate[1])
        return True
    def bob(nums, i):
        candidate = None
        for idx, x in enumerate(nums):
            if idx in removed: continue
            # Alice could remove this element in the next round
            if x <= k - i:
                if not candidate or x < candidate[0]:
                    candidate = (x, idx)
        if candidate:
            nums[candidate[1]] += k - i + 1
    for i in range(1, k+1):
        a = alice(nums, i)
        if not a:
            return False
        bob(nums, i)
    return True

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    low = 0
    high = 100
    while low < high:
        mid = (low + high) >> 1
        if play(nums[:], mid):
            low = mid + 1
        else:
            high = mid
    print(low-1)
