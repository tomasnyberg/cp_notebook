import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

for line in lines[2::2]:
    xs = list(map(int, line.lstrip('0')))
    CS = cum_sum(xs)
    result = [0]*(len(xs))
    result[0] = xs[0]
    for i in range(len(xs)-1,0,-1):
        result[i] += CS[i]
        result[i-1] += result[i] // 10
        result[i] %= 10
    print(''.join(map(str, result)).lstrip('0'))


