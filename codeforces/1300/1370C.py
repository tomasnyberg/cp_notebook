import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def prime(n):
    result = 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

a = "Ashishgup"
b = "FastestFinger"

for line in lines[1:]:
    num = int(line)
    if num == 1:
        print("FastestFinger")
        continue
    if num == 2 or num % 2 == 1:
        print("Ashishgup")
        continue
    if (num & (num-1)) == 0:
        print(b)
        continue
    print(b if num % 4 != 0 and prime(num//2) else a)