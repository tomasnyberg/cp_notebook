import sys
import itertools
lines = list(map(str.strip, sys.stdin.readlines()))

def best(s, length, target):
    curr = 0
    target_num = int(target, 2)
    for i in range(length):
        if s[i] == '1':
            curr |= 1 << (length - i - 1)
    shift_over_by = len(target) - length
    res = (curr << shift_over_by) | target_num
    for i in range(length, len(s)):
        # Set msb to 0
        curr &= ~(1 << (length - 1))
        curr <<= 1
        if s[i] == '1':
            curr |= 1
        res = max(res, (curr << shift_over_by) | target_num)
    return res
# print(bin(best("1110010", 2, "0010"))[2:])

s = lines[1]
trailingzeros = ''.join(list(itertools.dropwhile(lambda x: x == '1', s)))
start = s[0:len(s) - len(trailingzeros)]
low = 0
high = len(trailingzeros) + 1
biggest = 0
while low < high:
    # We want to cover at least the first mid zeroes
    mid = (low + high) >> 1
    needed = 0
    for i in range(mid):
        needed |= 1 << (len(trailingzeros) - i - 1)
    check = best(s, mid, trailingzeros)
    # print(bin(check)[2:], bin(needed)[2:], mid)
    if check >= needed:
        low = mid + 1
    else:
        high = mid
low -= 1
trailingzeros = list(trailingzeros)
for i in range(low):
    trailingzeros[i] = '1'
trailingzeros = ''.join(trailingzeros)
print(start + trailingzeros)
