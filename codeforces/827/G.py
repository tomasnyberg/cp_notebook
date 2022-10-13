import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def highest_bit(x, bitsset, idx):
    for i in range(31, -1,-1):
        if (1 << i) & x:
            bitsset[i].append((x, idx))

for line in lines[2::2]:
    bitsset = {i:[] for i in range(32)}
    nums = list(map(int, line.split(" ")))
    for idx,x in enumerate(nums):
        highest_bit(x, bitsset, idx)
    result = []
    taken = set([-1])
    running = 0
    for i in range(31, -1, -1):
        if running & (1 << i): continue
        if bitsset[i]:
            bitsset[i].sort(key=lambda x: x[0]^running)
            num, idx = -1, -1
            while idx in taken and bitsset[i]:
                num,idx = bitsset[i].pop()
            if idx in taken:
                continue
            running |= num
            result.append(num)
            taken.add(idx)
    # print(taken)
    for idx, x in enumerate(nums):
        if idx in taken: continue
        result.append(x)
    print(*result)
