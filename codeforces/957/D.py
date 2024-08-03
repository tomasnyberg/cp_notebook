import sys
from functools import lru_cache
if sys.argv[-1] == "--debug":
    sys.stdin = open("in")
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n, m, k = map(int, lines[ii].split())
    n += 1
    river = "L" + lines[ii+1]
    # next_log = [-1] * n
    # waiting = []
    # for i, x in enumerate(river):
    #     if x == 'W':
    #         waiting.append(i)
    #     elif x == 'L':
    #         for idx in waiting:
    #             next_log[idx] = i
    #         waiting = []
    #     elif x == 'C':
    #         waiting = []
    #     else:
    #         assert False
    # for idx in waiting:
    #     next_log[idx] = n
    i = 0
    total_swam = 0
    while i < len(river):
        if river[i] == 'W':
            total_swam += 1
            i += 1
        elif river[i] == 'L':
            for jump_len in range(1, m+1):
                if (i + jump_len == n) or (i + jump_len < n and river[i+jump_len] == 'L'):
                    i = i + jump_len
                    break
            else:
                for jump_len in range(m, 0, -1):
                    if i+jump_len < n and river[i+jump_len] == 'W':
                        i = i + jump_len
                        break
                else:
                    break
        elif river[i] == 'C':
            break
    if i == len(river) and total_swam <= k:
        print("YES")
    else:
        print("NO")
