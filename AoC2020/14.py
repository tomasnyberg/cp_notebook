import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def apply_mask(mask, num):
    s = mask[::-1]
    print(s)
    for i in range(len(s)):
        if s[i] == 'X':
            continue
        if s[i] == '0':
            if num & (1 << i):
                num &= ~(1 << i)
        if s[i] == '1':
            num |= (1 << i)
    return num

currmask = ''
mem = {}
for line in lines:
    split = line.split(" ")
    if split[0] == 'mask':
        currmask = split[2]
    else:
        addressbit = int(split[0][4:-1])
        value = int(split[-1])
        mem[addressbit] = apply_mask(currmask, value)

result = 0
for key,val in mem.items():
    result += val
print(result)
