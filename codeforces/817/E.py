import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, q = map(int, lines[i].split(" "))
    i+=1
    rectangles = []
    while n > 0:
        rectangles.append(list(map(int, lines[i].split(" "))))
        i+=1
        n-=1
    queries = []
    while q > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        i+=1
        q-=1
    for hs, ws, hb, wb in queries:
        result = 0
        for h, w in rectangles:
            if h > hs and h < hb and ws < w < wb:
                result += h*w
        print(result)  
