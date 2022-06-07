import sys
lines = list(map(str.strip, sys.stdin.readlines()))
i = 1
while i < len(lines):
    s = int(lines[i])
    intervals = []
    smallest = float("inf")
    biggest = 0
    cost_of_smallest = 0
    cost_of_biggest = 0
    for j in range(i+1, i+s+1):
        start, end, cost = map(int, lines[j].split(" "))
        if start <= smallest:
            if start < smallest:
                cost_of_smallest = cost 
                smallest = start
            else:
                cost_of_smallest = min(cost, cost_of_smallest) # Change
        if end >= biggest:
            if end > biggest:
                biggest = end
                cost_of_biggest = cost
            else:
                cost_of_biggest = min(cost_of_biggest, cost) # Change
        print(cost_of_biggest + cost_of_smallest)
    i += s+1