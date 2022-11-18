import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def zeroes(x):
    stringed = str(x)
    result = 0
    for c in stringed[::-1]:
        if c != '0': break
        result += 1
    return result
        
for line in lines[1:]:
    n, m = map(int, line.split(" "))
    best = [-1,-1]
    for i in range(1, m+1):
        z = zeroes(n*i)
        if z >= best[0]:
            best = [z, i]
    print(n*best[1], "was best for", n, "(times)", best[1])
        
        
    