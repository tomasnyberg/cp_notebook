import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def good_str(s, n0, n1, n2):
    counts = {0:n0, 1: n1, 2:n2}
    count = 0
    left = 0
    right = 0
    while right < len(s):
        count += int((s[right]))
        if right - left > 0:
            counts[count] -= 1
            count -= int(s[left])
            left += 1
        right += 1
    return (counts[0] == 0 and counts[1] == 0 and counts[2] == 0)


for line in lines[1:]:
    n0, n1, n2 = map(int, line.split(" "))
    res = ""
    if n1 == 0:
        print("0"*(n0 + 1) if n0 != 0 else "1"*(n2+1))
        continue
    if n1 % 2 == 0:
        res = "10" * (n1 // 2) #We have 1 too little n1 after this
        res = "1"*n2 + res
        res = "0"*(n0 + 1) + res
    if n1 % 2 == 1:
        res = "10"*((n1+1)//2) # We have just the right amount of n1
        res += '0' * n0
        res = '1' * n2 + res
    # assert(good_str(res, n0, n1, n2))
    print(res)
