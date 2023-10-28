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

for ii in range(1, len(lines), 3):
    n, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii+1].split()))
    h = list(map(int, lines[ii+2].split()))
    good_subs = []
    curr = []
    curr_vals = []
    for x, y in zip(h, a):
        if not curr or curr[-1] % x == 0:
            curr.append(x)
            curr_vals.append(y)
        else:
            good_subs.append(curr_vals)
            curr_vals = [y]
            curr = [x]
    good_subs.append(curr_vals)
    for i in range(len(good_subs)):
        good_subs[i] = cum_sum(good_subs[i])
    def check(mid):
        for subcs in good_subs:
            for i in range(len(subcs)):
                end = i + mid - 1
                if end >= len(subcs):
                    break
                if subcs[end] - (subcs[i-1] if i > 0 else 0) <= k:
                    # print(subcs, i, end, mid)
                    return True
        return False
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            low = mid + 1
        else:
            high = mid
    print(max(0, low - 1))