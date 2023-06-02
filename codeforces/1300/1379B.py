import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def find_numbers(l, r, m, n):
    a = m // n
    if a < l:
        a = l
    if a > r:
        a = r
    for candidate in [a, a+1, a-1]:
        if not l <= candidate <= r: continue
        curr = candidate * n
        diff = m - curr
        if abs(diff) > abs(r - l):
            continue# This tells us where to go in our binary search
        if diff < 0:
            b = l
            c = l - diff
        else:
            b = r
            c = r - diff
        return (candidate, b, c)
    return False


for line in lines[1:]:
    l, r, m = map(int, line.split())
    found = False
    low = 1
    high = m
    for n in range(1, m+1):
        res = find_numbers(l, r, m, n)
        if res:
            print(*res)
            break
    # while low < high:
    #     n = (low + high) // 2
    #     print(n, a,b,c)
    #     if b != -1:
    #         found = True
    #         break
    #     if a:
    #         high = n
    #     else:
    #         low = n + 1
    # print(*find_numbers(l, r, m, ((low + high) // 2)))
        


        
            
