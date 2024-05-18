import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


for ii in range(1, len(lines), 2):
    n, k, _ = map(int, lines[ii].split())
    s = lines[ii+1]
    def check(mid):
        target = s[:mid]
        curr = 0
        count = 0
        for c in s:
            if c == target[curr]:
                curr += 1
                if curr == mid:
                    count += 1
                    curr = 0
            else:
                curr = 0
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

        
