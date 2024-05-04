import sys
from collections import deque
# lines = list(map(str.strip, sys.stdin.readlines()))
lines = list(map(lambda x: x.strip(), open("/home/tomas/stuff/cp_notebook/codeforces/938/in").readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    xs = list(map(int, line))
    def check(k, xs=xs[:]):
        flipped = 0
        dq = deque()
        for i in range(len(xs)):
            if len(xs) - i >= k:
                if i >= k:
                    if dq.popleft() == 1:
                        flipped -= 1
                xs[i] += flipped
                xs[i] %= 2
                if xs[i] == 0:
                    flipped += 1
                    dq.append(1)
                    xs[i] = 1
                else:
                    dq.append(0)
            else:
                if i >= k and dq:
                    flipped -= dq.popleft()
                xs[i] += flipped
                xs[i] %= 2
        #     print(dq)
        # print(xs)
        return all(x == 1 for x in xs)
    # print("\n\n\n")
    low = 1
    high = len(xs)
    while low < high:
        mid = (low + high) // 2
        # print(mid, xs)
        if check(mid):
            low = mid + 1
        else:
            high = mid
    print(low)

