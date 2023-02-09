import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def sum_digits(x):
    return sum(map(int, str(x)))

def find_two(x):
    turn = 0
    listed = str(x)
    listed = list(map(int, listed))
    a = [0]*len(listed)
    b = [0]*len(listed)
    for i in range(len(listed)):
        while listed[i] > 0:
            if turn == 0:
                a[i] += 1
                listed[i] -= 1
                turn = 1
            else:
                b[i] += 1
                listed[i] -= 1
                turn = 0
    return int(''.join(map(str, a))), int(''.join(map(str, b)))
    

for line in lines[1:]:
    x = int(line)
    if x % 2 == 0:
        print(x//2, x//2)
    else:
        a, b = find_two(x)
        print(a, b)
    
    

