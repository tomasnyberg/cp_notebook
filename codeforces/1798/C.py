import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def prime_factors(x):
    counts = {}
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x //= i
            counts[i] = counts.get(i, 0) + 1
    return counts

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
        curr_gcd = curr_a * curr_target
        while b:
            target = lcm(curr_target, b[0])
            curr_gcd = gcd(curr_gcd, a[0] * b[0])
            # print("Target", target, a[0], b[0])
            if curr_gcd % target == 0:
                a.popleft()
                b.popleft()
                curr_target = target
            else:
                break
        # print(merged)
        result += 1
    print(result)

    