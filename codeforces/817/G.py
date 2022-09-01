import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def xorall(xs, start):
    total = 0
    for x in xs[start::2]:
        total ^= x
    return total


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
    # print("even xor", xorall(result, 0), "odd xor", xorall(result, 1))
    print(*result)
    # Print the binary representation of all numbers in result
    # [print(bin(x), end=" ") for x in result]
    # print()


    
    
