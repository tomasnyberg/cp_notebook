import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

# dp, we can choose every previous child
# so i times the current element - the running sum
MOD = 998_244_353

def faculty(n):
    result = 1
    while n > 0:
        result *= n
        result %= MOD
        n-=1
    return result

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    n = len(nums)
    nums.sort(reverse=True)
    result = 0
    total_dynasties = faculty(n-1)
    # print("total dynasties", total_dynasties)
    running = 0
    for i, x in enumerate(nums):
        if i == 0:
            running += x
            continue
        weight = total_dynasties * pow(i, MOD - 2, MOD) % MOD
        cost_across_all = running - (i)*x
        running += x
        result += cost_across_all * weight
        result %= MOD
    print(result)

