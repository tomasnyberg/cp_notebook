import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def best_choice(nums, curr):
    best = 100000000000
    pos = -1
    for idx, num in enumerate(nums):
        if best > abs(curr - num):
            best = abs(curr - num)
            pos = idx
    return pos

for i in range(1, len(lines), 3):
    best_seen = float("inf")
    n = int(lines[i])
    top = list(map(int, lines[i+1].split(" ")))
    bottom = list(map(int, lines[i+2].split(" ")))
    ways_to_connect_first = [0, best_choice(bottom, top[0]), n-1]
    ways_to_connect_last = [0, best_choice(bottom, top[-1]), n-1]
    for first_conn in ways_to_connect_first:
        for last_conn in ways_to_connect_last:
            # Connect a[0] and a[-1] and add the cost
            curr = abs(top[0] - bottom[first_conn]) + abs(top[-1] - bottom[last_conn])
            if first_conn > 0 and last_conn > 0: # b[0] isn't connected
                curr += abs(bottom[0] - top[best_choice(top, bottom[0])]) # Add the cost of connecting b[0]
            if first_conn < n-1 and last_conn < n-1: # b[-1] isn't connected
                curr += abs(bottom[-1] - top[best_choice(top, bottom[-1])]) # Add the cost of connecting b[-1]
            best_seen = min(best_seen, curr)
    print(best_seen)