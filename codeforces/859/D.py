import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

i = 1
while i < len(lines):
    n, q = map(int, lines[i].split())
    i+=1
    nums = list(map(int, lines[i].split()))
    queries = []
    i+=1
    for _ in range(q):
        queries.append(list(map(int, lines[i].split())))
        i+=1
    CS = cum_sum(nums)
    # print(nums)
    # print(CS)
    for l, r, k in queries:
        l -= 1
        r -= 1
        left = CS[l-1] if l-1 >= 0 else 0
        right = CS[-1] - CS[r] if r+1 < len(CS) else 0
        length = r-l+1
        parity = (length * k) % 2
        if parity + ((left + right) % 2) == 1:
            print("YES")
        else:
            print("NO")
