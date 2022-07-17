import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def transform(a, b):
    b % a == 0

for line in lines[1:]:
    a, b, c = map(int, line.split(" "))
    if a == b == c:
        print("YES")
        continue
    a_target = b - (c - b) if c >= b else b + (b-c)
    if a_target > 0 and a_target % a == 0:
        print("YES")
        continue
    c_target = b - (a - b) if a >= b else b + (b-a)
    if c_target > 0 and c_target % c == 0:
        print("YES")
        continue
    b_target = c - (c-a)/2 if c >= a else a - (a-c)/2
    if b_target > 0 and b_target % b == 0:
        print("YES")
        continue
    print("NO")