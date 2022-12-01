import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def apply_mask(mask, num):
    s = mask[::-1]
    for i in range(len(s)):
        if s[i] == 'X':
            continue
        if s[i] == '0':
            if num & (1 << i):
                num &= ~(1 << i)
        if s[i] == '1':
            num |= (1 << i)
    return num

def generate_all_memory(mask, address):
    s = mask[::-1]
    for i in range(len(s)):
        if s[i] == '1':
            address |= (1 << i)
    result = set([address])
    for i in range(len(s)):
        print(len(result))
        if s[i] == 'X':
            to_add = set()
            for sub in result:
                if sub & (1 << i):
                    to_add.add(sub & (~(1 << i)))
                else:
                    to_add.add(sub | (1 << i))
            result |= to_add
    return result
new = generate_all_memory("000000000000000000000000000000X1001X", 42)
print(list((x) for x in new))

currmask = ''
mem = {}
for line in lines:
    split = line.split(" ")
    if split[0] == 'mask':
        currmask = split[2]
    else:
        addressbit = int(split[0][4:-1])
        value = int(split[-1])
        addresses = generate_all_memory(currmask, addressbit)
        print(len(addresses))
        for address in addresses:
            mem[address] = value
        # mem[addressbit] = apply_mask(currmask, value)

result = 0
for key,val in mem.items():
    result += val
print(result)
