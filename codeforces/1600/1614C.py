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
    or_value = 0
    while m:
        or_value |= list(map(int, lines[i].split(" ")))[-1]
        m -= 1
        i += 1
    print(or_value * pow(2, n-1, 1000000007) % 1000000007)