import sys
lines = list(map(str.strip, sys.stdin.readlines()))


a = 2
while a < len(lines):
    m, n = map(int, lines[a].split(" "))
    a+=1
    ncopy = m
    matrix = []
    high = -1
    while ncopy > 0:
        matrix.append(list(map(int, lines[a].split(" "))))
        high = max(max(list(map(int ,lines[a].split(" ")))), high)
        ncopy-=1
        a+=1
    a+=1
    low = 1
    # print("low and high", low, high)
    def check(x):
        able = [False]*n
        pair = False
        for i in range(m):
            count = 0
            for j in range(n):
                if matrix[i][j] >= x:
                    able[j] = True
                    count +=1
            if count > 1: pair = True
        if not pair and m > 1: return False
        return all(able)
    while low <= high:
        mid = (high + low) >> 1
        if check(mid):
            low = mid + 1
        else:
            high = mid - 1
    print(low-1)