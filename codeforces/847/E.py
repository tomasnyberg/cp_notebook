import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(x):
    # for i in range(1, 2*x):
    #     other = 2*x - i
    #     assert(other + i == 2*x)
    #     if i ^ other == x:
    #         print(i, other, bin(x)[2:])
    #         ibin = bin(i)[2:]
    #         otherbin = bin(other)[2:]
    #         while len(ibin) < len(otherbin):
    #             ibin = "0" + ibin
    #         while len(otherbin) < len(ibin):
    #             otherbin = "0" + otherbin
    #         print(ibin, otherbin)
    a = x
    b = 0
    remaining = x
    for i in range(35, -1,-1):
        if not (1 << i) & a:
            if 2*(1 << i) <= remaining:
                remaining -= 2*(1 << i)
                a |= 1 << i
                b |= 1 << i
    if (a + b) // 2 == x and a ^ b == x:
        print(a, b)
    else:
        print(-1)

for line in lines[1:]:
    x = int(line)
    solve(x)
