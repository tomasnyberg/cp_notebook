import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    a = []
    b = []
    for _ in range(n):
        c, d = map(int, lines[i].split())
        a.append(c)
        b.append(d)
        i+=1
    a = deque(a)
    b = deque(b)
    result = 0
    while a and b:
        curr_a = a.popleft()
        curr_target = b.popleft()
        merged = [(curr_a, curr_target)]
        while b:
            target = lcm(curr_target, b[0])
            # print("Target", target, a[0], b[0])
            if a[0] % (target//b[0]) == 0 and all(x % (target//y) == 0 for x, y in merged):
                merged.append((a.popleft(), b.popleft()))
                curr_target = target
            else:
                break
        # print(merged)
        result += 1
    print(result)

    