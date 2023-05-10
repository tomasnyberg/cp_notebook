import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def find(s):
    zero = -1
    for i in range(len(s)):
        if s[i] == '0':
            zero = i
            break
    if len(s) % 2 == 1 and zero == len(s) // 2:
        return (1, len(s), len(s) // 2 + 1, len(s))
    if zero < len(s) // 2:
        return (zero + 1, len(s), zero + 2, len(s))
    else:
        return(1, zero + 1, 1, zero)

for line in lines[2::2]:
    s = line
    print(*find(s))