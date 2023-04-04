import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def layer(x, y, n):
    middles = [n//2, n//2 + 1]
    xtomiddle = min(abs(x - middles[0]), abs(x - middles[1]))
    ytomiddle = min(abs(y - middles[0]), abs(y - middles[1]))    
    return max(xtomiddle, ytomiddle)

for line in lines[1:]:
    n, x1, y1, x2,y2 = map(int, line.split())
    # print(x1, y1, x2, y2)
    # print(layer(x1, y1, n))
    # print(layer(x2, y2, n))
    print(abs(layer(x1, y1, n) - layer(x2, y2, n)))