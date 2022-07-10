import sys
from heapq import heappop, heappush
lines = list(map(str.strip, sys.stdin.readlines()))

points = {}
for i in range(97, 123):
    points[chr(i)] = i - 96

def score_of_str(s):
    result = 0
    for c in s:
        result += points[c]
    return result


for i in range(1, len(lines),2 ):
    str = lines[i]
    target = int(lines[i+1])
    curr_score = score_of_str(str)
    removed_indices = set()
    hq = []
    for idx, c in enumerate(str):
        heappush(hq, (-points[c], idx))
    while curr_score > target:
        score, idx = heappop(hq)
        curr_score += score
        removed_indices.add(idx)
    result = ""
    for idx, c in enumerate(str):
        if idx not in removed_indices:
            result += c
    print(result)
