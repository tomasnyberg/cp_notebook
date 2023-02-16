import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from heapq import heappop, heappush


def expand(phq, qhq, pcurr, qcurr, p, q, left, right, steps, result):
    def check(pcurr, qcurr):
        while phq and phq[0] == pcurr + 1:
            pcurr += 1
            heappop(phq)
        while qhq and qhq[0] == qcurr + 1:
            qcurr += 1
            heappop(qhq)
        if pcurr == qcurr:
            result[0] += 1
        return pcurr, qcurr
    for _ in range(abs(steps)):
        if steps > 0:
            right += 1
            heappush(phq, p[right])
            heappush(qhq, q[right])
        else:
            left -= 1
            heappush(phq, p[left])
            heappush(qhq, q[left])
        pcurr, qcurr = check(pcurr, qcurr)
    pcurr, qcurr = check(pcurr, qcurr)
    return pcurr, qcurr, left, right

for i in range(1, len(lines), 2):
    p = list(map(int, lines[i].split()))
    q = list(map(int, lines[i + 1].split()))
    p_indices = {x: idx for idx, x in enumerate(p)}
    q_indices = {x: idx for idx, x in enumerate(q)}
    idx = p_indices[1]
    phq = [p[idx]]
    qhq = [q[idx]]
    result = [0]
    extra = 0
    pcurr, qcurr, left, right = expand(phq, qhq, 0, 0, p, q, idx, idx, 0, result)
    while pcurr != len(p) or qcurr != len(q):
        idx = p_indices[pcurr + 1] if pcurr <= qcurr else q_indices[qcurr + 1]
        steps = idx - right if idx > right else -(left - idx)
        if idx > right and pcurr == qcurr:
            extra += left
        elif idx < left and pcurr == qcurr:
            extra += len(p) - right - 1
        pcurr, qcurr, left, right = expand(phq, qhq, pcurr, qcurr, p, q, left, right, steps, result)
    result[0] //= 2
    result[0] += extra
    result = result[0]
    before = min(p_indices[1], q_indices[1])
    result += before*(before + 1)//2
    between = max(p_indices[1], q_indices[1]) - min(p_indices[1], q_indices[1]) - 1
    result += between*(between + 1)//2
    after = len(p) - max(p_indices[1], q_indices[1]) - 1
    result += after*(after + 1)//2
    print(result)
    

        
