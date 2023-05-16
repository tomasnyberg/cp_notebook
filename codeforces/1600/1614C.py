import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def generate_xor_sum(arr):
    result = 0
    n = len(arr)
    subseq_count = 2**(n-1)

    for num in arr:
        result ^= num * subseq_count

    return result

def generate_xor_sum_bf(arr):
    total = 0
    for i in range(2**len(arr)):
        result = 0
        for j in range(len(arr)):
            if i & (1 << j):
                result ^= arr[j]
        total += result
        # print(result, end=" ")
    return total

def xorSum(arr, n):
    bits = 0
    for i in range(n):
        bits |= arr[i]
    ans = bits * pow(2, n-1)
    ans %= 1000000007
    return ans

i = 1
while i < len(lines):
    n, m = map(int, lines[i].split(" "))
    i+=1
    segments = []
    while m:
        l, r, x = map(int, lines[i].split(" ")) 
        segments.append((l, r, x))
        m -= 1
        i += 1
    nums = [0]*(n + 1)
    for l, r, x in segments:
        nums[r] = x
    subseqs = 0
    segments.sort(key=lambda x: x[1])
    for l, r, x in segments:
        nums[r] = max(nums[r], x)
    nums.pop(0)
    print(xorSum(nums, n) % 1000000007)