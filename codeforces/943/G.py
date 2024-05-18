import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

def z_function(target, s):
    prefixed = target + s
    z = [0] * len(prefixed)
    left = right = 0
    for i in range(1, len(prefixed)):
        if i < right:
            z[i] = min(right - i, z[i-left])
        while i + z[i] < len(prefixed) and prefixed[i + z[i]] == prefixed[z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z[len(target):]

for ii in range(1, len(lines), 2):
    n, k, _ = map(int, lines[ii].split())
    s = lines[ii+1]
    def check(mid):
        target = s[:mid]
        Z = z_function(target, s)
        i = 0
        count = 0
        while i < n:
            if Z[i] >= mid:
                count += 1
                i+=mid
            else:
                i+=1
        return count >= k
    low = 1
    high = n + 1
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            low = mid + 1
        else:
            high = mid
    print(low - 1)

        
