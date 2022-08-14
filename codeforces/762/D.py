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
    # Check whether we can reach min joy x for all friends
    # Do this by checking if we are able to buy all friends a gift with joy >= x, and
    # also that we can buy two gifts from the same store. If we can buy two gifts from the same store
    # and also one for every friend then we are good.
    # The "2 from the same store" argument works since we can visit n-1 stores, meaning that if two can be
    # bought from the same store we can just pick whatever good store for the rest of our friends
    def check(x):
        able = [False]*n # Are we able to buy all friends 1-n a gift with joy >= x?
        pair = False # Are we able to buy two gifts with joy >= x in the same store?
        for i in range(m):
            count = 0 # How many friends for which we can buy a gift with joy >= x 
            for j in range(n):
                # We can buy a gift with joy >= x for friend j
                if matrix[i][j] >= x:
                    able[j] = True
                    count +=1
            # This store has 2 "good gifts" meaning our second criteria is fulfilled
            if count > 1: pair = True
        return all(able) and pair
    while low <= high:
        mid = (high + low) >> 1
        if check(mid):
            low = mid + 1
        else:
            high = mid - 1
    print(low-1)