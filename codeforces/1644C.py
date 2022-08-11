import sys
lines = list(map(str.strip, sys.stdin.readlines()))

INF = 10**9
for i in range(1, len(lines), 2):
    n, x = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    # The max subarrays of lengths 0 -> n
    max_sa_of_len_n = [INF for j in range(n+1)]
    max_sa_of_len_n[0] = 0 # The subarray of length 0
    for l in range(1, n+1):
        s = sum(nums[:l])
        best = s
        for j in range(l, len(nums)):
            s += nums[j]
            s -= nums[j - l]
            best = max(best, s)
        max_sa_of_len_n[l] = best
    for k in range(0, n+1):
        best = 0
        for l in range(1, n+1):
            best = max(best, min(l, k)*x + max_sa_of_len_n[l])
        print(best, end=" ")
    print()