import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from collections import deque

ii = 1
while ii < len(lines):
    a = list(lines[ii])
    b = list(lines[ii+1])
    strings = [a, b]
    ii += 2
    t, q = map(int, lines[ii].split())
    ii+=1
    notequal = set()
    for i in range(len(a)):
        if a[i] != b[i]:
            notequal.add(i)
    time = 0
    blocked = deque()
    for i in range(q):
        query = list(map(int, lines[ii+i].split()))
        time +=1
        while blocked and blocked[0] <= time:
            idx = blocked.popleft()
            if a[idx] != b[idx]:
                notequal.add(idx)
        if query[0] == 1:
            blocked.append(query[1]-1)
            notequal.discard(query[1]-1)
        elif query[0] == 2:
            first_idx, a_swap, second_idx, b_swap = query[1]-1, query[2]-1, query[3]-1, query[4]-1
            strings[first_idx][a_swap], strings[second_idx][b_swap] = strings[second_idx][b_swap], strings[first_idx][a_swap]
            for idx in [a_swap, b_swap]:
                if a[idx] != b[idx]:
                    notequal.add(idx)
                else:
                    notequal.discard(idx)
        else:
            print("YES" if len(notequal) == 0 else "NO")
    ii += q