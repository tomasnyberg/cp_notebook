import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b = map(int, line.split())
    # print(a, b)
    maxlen = max(len(bin(a)[2:]), len(bin(b)[2:]))
    # print(bin(a)[2:].zfill(maxlen) + "\n" + bin(b)[2:].zfill(maxlen))
    for i in range(32):
        if (1 << i) & a and (1 << i) & b:
            a ^= (1 << i)
            b ^= (1 << i)
    # print("\n" + bin(a)[2:].zfill(maxlen) + "\n" + bin(b)[2:].zfill(maxlen))
    biggest_a_bit = -1
    biggest_b_bit = -1
    for i in range(32):
        if (1 << i) & b:
            biggest_b_bit = i
        if (1 << i) & a:
            biggest_a_bit = i
    for i in range(biggest_a_bit + 1, biggest_b_bit + 1):
        if (1 << i) & b:
            b ^= (1 << i)
    print(a - b + 1)
    
    
    

        