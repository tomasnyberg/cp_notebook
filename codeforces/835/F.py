import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

def bs(CS, d, c):
    def check(k):
        if k < len(CS):
            return CS[k]*(d//(k+1)) + CS[d % (k+1)] >= c
        else:
            total_cycle = CS[-1]*(d//k+1)
            unfinished_days = d % k
            if unfinished_days >= len(CS):
                unfinished_days = len(CS) - 1
            additional = CS[unfinished_days]
            return total_cycle + additional >= c 
    low = 0
    high = 10**16 # I think it makes sense to have a hughe high? Does not make it slower really
    while low < high:
        mid = (low + high) >> 1
        # print("checking", mid, check(mid))
        if check(mid):
            low = mid + 1
        else:
            high = mid
    return low 

for i in range(1, len(lines), 2):
    n, c, d = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    nums.sort(key=lambda x: -x)
    CS = cum_sum(nums)
    if CS[d-1 if d-1 < len(CS) else -1] >= c:
        print("Infinity")
        continue
    if nums[0] * d < c:
        print("Impossible")
        continue
    print(CS)
    print(bs(CS, d, c))
    