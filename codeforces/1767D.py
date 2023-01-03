import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))

n = int(lines[0])
s = lines[1]

ones = sum(1 for c in s if c == '1')
zeroes = sum(1 for c in s if c == '0')
result = []
# Function to count the number of bits ina number
def countBits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

for i in range(1, 2**n + 1):
    oc = ones 
    zc = zeroes
    bigger = 2**n - i
    smaller = i - 1 
    # print("\n\n", i)
    for c in s:
        # print("Before", c, "Smaller", smaller, "bigger", bigger)
        if c == '1':
            smaller -= 1 # from eq
            smaller -= bigger % 2
            smaller //= 2
            if smaller < 0:
                break
            if countBits(1 + smaller + bigger) != 1:
                if bigger % 2 == 1:
                    bigger += 1
                bigger //= 2
        else:
            bigger -= 1
            bigger -= smaller % 2
            bigger //= 2
            if bigger < 0:
                break
            if countBits(1 + smaller + bigger) != 1:
                if smaller % 2 == 1:
                    smaller += 1
                smaller //= 2
        # print("After", c, "Smaller", smaller, "bigger", bigger)
        # print()
    if smaller == 0 and bigger == 0:
        result.append(i)
print(*result)
    

    
            




