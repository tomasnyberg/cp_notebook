import sys
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, m = map(int, lines[i].split())
    m_nums = list(map(int, lines[i + 1].split()))
    hq = []
    for j in range(1, n+1):
        heappush(hq, -j + 1)
    seen = set()
    ans = [-1 for _ in range(n)]
    for j in range(len(m_nums)):
        if m_nums[j] in seen: continue
        seen.add(m_nums[j])
        if not hq: continue
        x = heappop(hq)
        # print(j, -x)
        ans[-x] = j + 1
    # print("\n\n")
    print(*ans)

