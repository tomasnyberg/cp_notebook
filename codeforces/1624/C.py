import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def find_rest(needed, available):
    for i in range(len(available)):
        key = available[i][0]
        possible = set()
        while key > 0:
            possible.add(key)
            key >>= 1
        available[i].append(possible)
    while needed:
        curr = needed.pop()
        found = False
        for i in range(len(available)):
            x, amount, possible = available[i]
            if amount == 0: continue
            if curr in possible:
                available[i][1] -= 1
                found = True
                break
        if not found:
            print("NO")
            return
    print("YES")




for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    n = len(nums)
    needed = set([i for i in range(1, n +1)])
    already_used = [False]*n
    nums.sort(key=lambda x: -x)
    for idx, x in enumerate(nums):
        if already_used[idx]: continue
        if x <= n and x in needed:
            needed.remove(x)
            already_used[idx] = True
    if len(needed) == 0:
        print("YES")
        continue
    needed = list(sorted(list(needed)))
    available = {}
    for idx, x in enumerate(nums):
        if already_used[idx]: continue
        available[x] = 1 if x not in available else available[x] + 1
    available = list(sorted([[key, available[key]] for key in available], key=lambda x:-x[0]))
    find_rest(needed, available)