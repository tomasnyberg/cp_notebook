import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def select_best(intervals):
    smallest = float("inf")
    biggest = 0
    for start, end, cost in intervals:
        smallest = min(start, smallest)
        biggest = max(end, biggest)
    start_candidate = (float("inf"), -1, -1) # Cost, index in intervals, endpoint
    end_candidate = (float("inf"), -1, -1) # Cost, index in intervals, startpoint
    for i in range(len(intervals)):
        start, end, cost = intervals[i]
        if start == smallest and cost < start_candidate[0]:
            start_candidate = (cost, i, end)
        if end == biggest and cost < end_candidate[0]:
            end_candidate = (cost, i, start)
    if start_candidate[1] == end_candidate[1]:
        return start_candidate[0]
    if end_candidate[2] == smallest:
        return end_candidate[0]
    if start_candidate[2] == biggest:
        return start_candidate[0]
    return start_candidate[0] + end_candidate[0]

i = 1
while i < len(lines):
    s = int(lines[i])
    intervals = []
    for j in range(i+1, i+s+1):
        intervals.append(list(map(int, lines[j].split(" "))))
        print(select_best(intervals))
    i += s+1