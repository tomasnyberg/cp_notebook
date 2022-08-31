import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for x in lines[1:]:
    x = int(x)
    result = []
    for i in range(x-3):
        result.append(i+1)
    result.append(1 << 29)
    result.append(1 << 30)
    last = 0
    for x in result:
        last ^= x
    result.append(last)
    print(*result)

    
    
