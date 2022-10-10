import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n, l, r, s = map(int, line.split(" "))
    nums = r - l + 1
    total = sum([i for i in range(n-nums+1, n+1)])
    steps = int(math.ceil(((total - s)/nums)))
    total -= steps*nums
    if n-nums+1 - steps <= 0 or steps < 0:
        print(-1)
        continue
    candidates = [i for i in range(n-nums+1-steps, n-steps+1)]
    currsum = sum(candidates)
    # print(candidates)
    for i in range(len(candidates)-1,-1,-1):
        if currsum == s:
            break
        next = 10**9+7 if i == len(candidates) - 1 else candidates[i+1]
        to_add = min(n-candidates[i], s - currsum, next - candidates[i] - 1)
        candidates[i] += to_add
        currsum += to_add 
    if sum(candidates) != s:
        print(-1)
        continue
    taken = set(candidates)
    result = [-1 for i in range(n)]
    a = 0
    for i in range(l-1, r):
        result[i] = candidates[a]
        a+=1
    i = 1
    while i in taken:
        i+=1
    # print(result)
    for j in range(len(result)):
        if result[j] != -1: continue
        result[j] = i
        taken.add(i)
        while i in taken:
            i+=1
    print(*result)


