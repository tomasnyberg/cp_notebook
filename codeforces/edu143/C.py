import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import bisect

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for i in range(1, len(lines), 3):
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+2].split()))
    CS = cum_sum(b)
    line = [0] * (len(a) + 1)
    result = [0] * (len(a))
    for j in range(len(a)):
        # this tea drinker can drink the whole thing
        if b[j] >= a[j]:
            # print("index", j, "can drink the whole thing")
            result[j] += a[j]
            continue
        look_for = a[j] + (CS[j-1] if j > 0 else 0)
        # binary search for the first index where CS[idx] >= look_for
        idx = bisect.bisect_left(CS, look_for)
        line[j] += 1
        if idx == len(CS):
            # print("Everyone will drink full from", j)
            continue
        line[idx] -= 1
        remaining = a[j] - (CS[idx-1] - (CS[j-1] if j > 0 else 0))
        result[idx] += remaining
        # print("index", idx, "will drink the remaining", remaining)
    # print("line", line)
    running = 0
    for j in range(len(a)):
        running += line[j]
        result[j] += running*b[j]
    print(*result)




    
