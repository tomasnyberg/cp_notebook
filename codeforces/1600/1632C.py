import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def print_binaries(a, b):
    maxlen = max(len(bin(a)[2:]), len(bin(b)[2:]))
    print(bin(a)[2:].zfill(maxlen) + "\n" + bin(b)[2:].zfill(maxlen))
    print("---")


for line in lines[1:]:
    a, b = map(int, line.split())
    # print(a, b)
    candidate = b - a
    # print("Numbers:", a,b, "Initial:")
    # print_binaries(a, b)
    for i in range(32):
        if (1 << i) & a and (1 << i) & b:
            a ^= (1 << i)
            b ^= (1 << i)
    # print("after taking mutual:")
    # print_binaries(a, b)
    biggest_a_bit = -1
    biggest_b_bit = -1
    for i in range(32):
        if (1 << i) & b:
            biggest_b_bit = i
        if (1 << i) & a:
            biggest_a_bit = i
    add = 0
    for i in range(biggest_a_bit + 1, biggest_b_bit + 1):
        if (1 << i) & b:
            add = 1
            b ^= (1 << i)
    # print("After truncating b")
    # print_binaries(a, b)
    print(min(a - b + add, candidate))
    
    
    

        