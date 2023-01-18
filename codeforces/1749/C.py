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
    res = 0
    for k in range(0, 101):
        if play(nums[:], k):
            res = k
    print(res)
