import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# lines = open('codeforces/929/in').read().splitlines()
# TODO Remember to add int wrapping if using dict

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

ii = 2
while ii < len(lines):
    nums = list(map(int, lines[ii].split()))
    CS = cum_sum(nums)
    ii+=1
    q = int(lines[ii])
    ii+=1
    queries = []
    for _ in range(q):
        l, r = map(int, lines[ii].split())
        queries.append((l, r))
        ii+=1
    ii+=1
    for l, u in queries:
        l-=1
        def check(mid):
            sections = CS[mid] - (CS[l-1] if l > 0 else 0)
            return sections >= u
        def f(x):
            return x*(x+1) // 2
        def score(pos):
            sections = CS[pos] - (CS[l-1] if l > 0 else 0)
            diff = u - sections
            if diff < 0:
                return f(u) - f(-diff - 1)
            return f(u) - f(diff)
        low = l + 1
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        best = [-10**9, -1]
        cands = []
        for d in range(10, -10, -1):
            if l <= low + d < len(nums):
                cand = score(low + d)
                cands.append((low + d, cand))
                if cand >= best[0]:
                    best = [cand, low + d + 1]
        print(best[-1], end=" ")
        # print("cands", cands)
        # print()
    print()