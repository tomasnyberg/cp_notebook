import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    ends = {i: 0 for i in range(10)}
    found = False
    for num in nums:
        ends[num%10] += 1
    for i in range(10):
        if ends[i] == 0: continue
        ends[i] -= 1
        for j in range(10):
            if ends[j] == 0: continue
            ends[j] -= 1
            for k in range(10):
                if ends[k] == 0: continue
                if (i + j + k )%10 == 3:
                    found = True
            ends[j] += 1
        ends[i] += 1
    if found:
        print("YES")
    else:
        print("NO")
    
