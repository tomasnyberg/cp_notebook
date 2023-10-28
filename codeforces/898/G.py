import sys
from functools import lru_cache
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    s = list(line)
    if all(c == 'A' for c in s):
        print(0)
        continue
    result = 0
    # print(''.join(s))
    indices = [i for i in range(len(s)) if s[i] == 'B']
    @lru_cache(None)
    def dp(i, prev_taken):
        if i == len(indices):
            return 0
        # Take to the right
        if prev_taken:
            if i == len(indices) - 1:
                return len(s) - indices[i] - 1
            return indices[i+1] - indices[i] - 1 + dp(i+1, True)
        previous = indices[i-1] if i > 0 else -1
        take_previous = indices[i] - previous - 1 + dp(i+1, False)
        take_next = (len(s) - indices[i] if i == len(indices) - 1 else indices[i+1] - indices[i]) - 1 + dp(i+1, True)
        return max(take_previous, take_next)
    print(dp(0, False))
