import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    result = 0
    for bit in range(61):
        if (1 << bit) > n: break
        # print("bit",bit,"contributes with", n//(bit+1))
        result += (n) // (1 << bit)
    print(result)
