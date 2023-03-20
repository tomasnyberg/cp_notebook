import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    evens = [n for n in nums if n % 2 == 0]
    odds = [n for n in nums if n % 2 == 1]
    xs = evens + odds
    a = 0
    b = 0
    for x in xs:
        if x % 2 == 0:
            a += x
        else:
            b += x
        if a <= b:
            print("NO")
            break
    else:
        print("YES")