import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result


for ii in range(1, len(lines), 3):
    n = int(lines[ii])
    xs = list(map(int, lines[ii+1].split()))
    s = lines[ii+2]
    l_found = False
    CS = cum_sum(xs)
    l_s = [i for i in range(n) if s[i] == 'L'][::-1]
    r_s = [i for i in range(n) if s[i] == 'R']
    result = 0
    while l_s and r_s:
        if l_s[-1] > r_s[-1]:
            l_s.pop()
            continue
        if r_s[-1] < l_s[-1]:
            r_s.pop()
            continue
        leftmost_l = l_s.pop()
        rightmost_r = r_s.pop()
        result += CS[rightmost_r] - (CS[leftmost_l - 1] if leftmost_l > 0 else 0)
    print(result)
