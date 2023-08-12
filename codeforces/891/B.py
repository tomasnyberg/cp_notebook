import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    s = line
    carry = 0
    s = list(map(int, s))
    roundfrom = len(s)
    for i in range(len(s) - 1, -1, -1):
        x = s[i] + carry
        if x == 10:
            s[i] = 0
            carry = 1
            continue
        if x >= 5:
            roundfrom = i
            s[i] = 0
            carry = 1
        else:
            s[i] = x
            carry = 0
            continue 
    for i in range(roundfrom, len(s)):
        s[i] = 0
    if carry:
        s.insert(0, 1)
    print("".join(map(str, s)))