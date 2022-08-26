import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 3):
    n, p, k = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1]))
    x, y = map(int, lines[i+2].split(" "))
    needtofillin = {j:0 for j in range(k)}
    # We cna start at k-1 since we shoot the ball over all the other ones
    for j in range(p-1, len(nums)):
        if not nums[j]: needtofillin[(j-(p-1))%k]+=1
    result = 10**9
    for offset in needtofillin:
        if n - offset >= p:
            result = min(result, offset*y+needtofillin[offset]*x)
    print(result)
    print(needtofillin)