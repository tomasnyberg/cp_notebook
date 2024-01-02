import sys
from collections import Counter
from heapq import heappush, heappop
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

class fenwick_tree:
    def __init__(self, values) -> None:
        values.insert(0, 0)
        n = len(values)
        self.tree = values.copy()
        for i in range(1, n):
            parent = i + (i & -i)
            if parent < n: self.tree[parent] += self.tree[i]
    
    def prefixSum(self, i):
        total = 0
        while i != 0:
            total += self.tree[i]
            i &= ~(i&-i)
        return total	
            
    def range_sum(self, left, right):
        assert left <= right, "left is not leq right"
        return self.prefixSum(right) - self.prefixSum(left - 1)
    
    def get(self, i):
        return self.range_sum(i, i)
    
    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i
    
    def set(self, i, val):
        self.add(i, val - self.range_sum(i, i))

ii = 1
while ii < len(lines):
    n = int(lines[ii])
    intervals = []
    ii += 1
    for _ in range(n):
        intervals.append(list(map(int, lines[ii].split())))
        ii+=1
    intervals.sort()
    starts = [x[0] for x in intervals]
    ends = [x[1] for x in intervals]
    allsorted = list(sorted(starts + ends))
    mapped = {}
    for i, x in enumerate(allsorted):
        mapped[x] = i+1
    fwt = fenwick_tree([0]*(len(allsorted)+1))
    for e in ends:
        fwt.add(mapped[e], 1)
    startends = {}
    startcounts = dict(Counter(starts))
    for s, e in intervals:
        if s not in startends:
            startends[s] = {}
        startends[s][e] = startends[s].get(e, 0) + 1
    result = 0
    for s in sorted(startends.keys()):
        for e in startends[s]:
            fwt.add(mapped[e], -startends[s][e])
        for e in startends[s]:
            result += fwt.range_sum(mapped[s], mapped[e])
        result += startcounts[s] * (startcounts[s] - 1) // 2
    print(result)
    