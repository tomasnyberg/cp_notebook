import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    chests = list(map(int, lines[i+1].split(" ")))
    CSR = list(reversed(cum_sum(list(reversed(chests)))))
    print(CSR)
    j = 0
    result = 0
    while j < len(chests) and ((CSR[j]) >> 1) > k:
        result += chests[j] - k
        j+=1
    multi = 2
    while j < len(chests):
        result += chests[j] // multi
        multi *= 2
        j+=1
    print(result)