import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappop, heappush


def expand(phq, qhq, pcurr, qcurr, p, q, left, right, steps):
    if steps < 0:
        for _ in range(-steps):
            left -= 1
            heappush(phq, p[left])
            heappush(qhq, q[left])
    else:
        for _ in range(steps):
            right += 1
            heappush(phq, p[right])
            heappush(qhq, q[right])
    while phq and phq[0] == pcurr + 1:
        pcurr += 1
        heappop(phq)
    while qhq and qhq[0] == qcurr + 1:
        qcurr += 1
        heappop(qhq)
    return pcurr, qcurr, left, right

for i in range(1, len(lines), 2):
    p = list(map(int, lines[i].split()))
    q = list(map(int, lines[i + 1].split()))
    p_indices = {x: idx for idx, x in enumerate(p)}
    q_indices = {x: idx for idx, x in enumerate(q)}
    idx = p_indices[1]
    phq = [p[idx]]
    qhq = [q[idx]]
    pcurr, qcurr, left, right = expand(phq, qhq, 0, 0, p, q, idx, idx, 0)
    while pcurr != len(p) or qcurr != len(q):
        idx = p_indices[pcurr + 1] if pcurr <= qcurr else q_indices[qcurr + 1]
        steps = idx - right if idx > right else -(left - idx)
        pcurr, qcurr, left, right = expand(phq, qhq, pcurr, qcurr, p, q, left, right, steps)

        
