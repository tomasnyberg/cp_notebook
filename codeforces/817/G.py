import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for x in lines[1:]:
    x = int(x)
    counter = 1
    result = []
    BIGNUMS = 0
    for i in range(x-1 if x % 2 == 1 else x):
        if i%2 == 0:
            result.append((1 << 29) + counter)
            BIGNUMS += 1
        else:
            result.append(counter)
            counter+=1
    if x % 2 == 1:
        if BIGNUMS % 2 == 1:
            result.append((1<<29))
        else:
            result.append(0)
    else:
        if BIGNUMS % 2 == 1:
            result[2] += (1 << 30)
            result[0] += (1 << 30)
            result[0] -= (1 << 29)
    print(*result)


    
    
