import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def cumsum2d(arr):
    result = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[0])):
            sum += arr[i][j]
            result[i][j] = sum + (result[i-1][j] if i > 0 else 0)
    return result

i = 1
while i < len(lines):
    n, q = map(int, lines[i].split(" "))
    i+=1
    rectangles = []
    maxh= 0
    maxw = 0
    while n > 0:
        rectangles.append(list(map(int, lines[i].split(" "))))
        maxh= max(maxh, rectangles[-1][0])
        maxw = max(maxw, rectangles[-1][1])
        i+=1
        n-=1
    queries = []
    while q > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        maxh = max(maxh, queries[-1][2])
        maxw = max(maxw, queries[-1][3])
        i+=1
        q-=1
    rectanglematrix = [[0 for i in range(maxw+2)] for j in range(maxh+2)]
    for h, w in rectangles:
        rectanglematrix[h][w] += h*w
    twodcumsum = cumsum2d(rectanglematrix)
    # for xs in twodcumsum:
    #     print(*xs)
    for hs, ws, hb, wb in queries:
        hs += 1
        ws += 1
        hb -= 1
        wb -= 1
        bottomright = twodcumsum[hb][wb]
        topright = twodcumsum[hs-1][wb] if hs > 1 else 0
        bottomleft = twodcumsum[hb][ws-1] if ws > 1 else 0
        topleft = twodcumsum[hs-1][ws-1] if hs > 1 and ws > 1 else 0
        print(bottomright - topright - bottomleft + topleft)
        # print(result)  
