import sys

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

def solve():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    CS = cum_sum(nums)
    low = 1
    high = n
    # print(CS)
    while low < high:
        mid = (low+high)//2
        print("?", mid, *[i for i in range(1, mid+1)], flush=True)
        sys.stdout.flush()
        sum1 = int(sys.stdin.readline())
        if sum1 <= CS[mid-1]:
            low = mid+1
        else:
            high = mid
    print("!", low, flush=True)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
# 2
# 5
# 1 2 3 4 5