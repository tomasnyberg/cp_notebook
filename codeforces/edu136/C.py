import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

MOD = 998244353

def nCr(n,r):
    return math.factorial(n) // (math.factorial(r)*(math.factorial(n-r)))

for line in lines[1:]:
    n = int(line)
    template = "AABB"
    idx = 3
    draw_line = ""
    for _ in range(n):
        draw_line += template[idx]
        idx = (idx + 1) % 4
    assert(len(draw_line) == n)
    a_win = 0
    b_win = 0
    a_remaining = n // 2
    b_remaining = n // 2
    for i in range(n):
        if not a_remaining or not b_remaining:
            break
        remaining = n - i - 1
        if draw_line[i] == 'A':
            a_remaining -= 1
            b_win += nCr(remaining, b_remaining-1)
        else:
            b_remaining -= 1
            a_win += nCr(remaining, a_remaining-1)
    print(a_win % MOD, b_win % MOD, 1)


