import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

precounted = []

def count(x):
    result = 0
    for i in range(x+1):
        for j in range(x+1):
            for k in range(x+1):
                if i + j + k == x:
                    result += 1
    return result

for i in range(10):
    precounted.append(count(i))

for line in lines[1:]:
    n = int(line)
    cnt = 1
    while n > 0:
        d = n % 10
        n //= 10
        if d == 0:
            continue
        cnt *= precounted[d]
    print(cnt)