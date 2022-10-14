import sys
from queue import deque
lines = list(map(str.strip, sys.stdin.readlines()))

def all_windows(s, result):
    def sliding_window(xs, size, result):
        left = 0
        right = 0
        while right < len(xs):
            if right - left >= size - 1:
                result[xs[left:right+1]] = left+len(xs)-right-1
                left += 1
            right += 1
    for i in range(0, len(s)+1):
        sliding_window(s, i, result)
        
    

    
for i in range(1, len(lines), 2):
    a = (lines[i])
    b = (lines[i+1])
    asubstrs = {}
    bsubstrs = {}
    result = len(a) + len(b)
    all_windows(a, asubstrs)
    all_windows(b, bsubstrs)
    for ss in asubstrs:
        if ss in bsubstrs:
            result = min(result, asubstrs[ss] + bsubstrs[ss])
    # print(asubstrs, bsubstrs)
    # print("\n")
    print(result)