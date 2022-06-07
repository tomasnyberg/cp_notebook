import sys
lines = list(map(str.strip, sys.stdin.readlines()))
i = 1
while i < len(lines):
    s = int(lines[i])
    smallest = [float("inf"), float("inf")] # smallest integer and its cost
    biggest = [0, float("inf")] # biggest integer and its cost
    longest = [0, float("inf")] # Longest segment and the cost of it
    for j in range(i+1, i+s+1):
        start, end, cost = map(int, lines[j].split(" "))
        # Longest segment
        if end - start > longest[0]: longest = [end-start, cost]
        if end - start == longest[0]: longest[1] = min(cost, longest[1])
        # Smallest integer
        if start < smallest[0]: smallest = [start, cost]
        if start == smallest[0]: smallest[1] = min(cost, smallest[1])
        # Biggest
        if end > biggest[0]: biggest = [end, cost]
        if end == biggest[0]: biggest[1] = min(cost, biggest[1])
        if longest[0] == biggest[0] - smallest[0]:
            print(min(smallest[1] + biggest[1], longest[1]))
        else:
            print(smallest[1] + biggest[1])    
    i += s+1