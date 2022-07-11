import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    result = 0
    prev = 'ä'
    streak_of_ones = {} 
    streak = 1
    # print(line)
    for idx, c in enumerate(line):
        # print(c, streak, streak_of_ones, end="  ->  ")
        if c == prev:
            streak+=1
            streak_of_ones.clear()
            # print(streak, streak_of_ones)
            continue
        if c != prev and streak == 1: # need to handle what we started on somehow
            if c in streak_of_ones:
                result += idx - streak_of_ones[c] - 1
                streak = 2
                streak_of_ones.clear()
                # print(streak, streak_of_ones)
                continue
            streak_of_ones[c] = idx
            prev = c
        else:
            if streak % 2 == 1:
                result += 1
            streak = 1
            prev = c
            streak_of_ones = {c:idx}
        # print(streak, streak_of_ones)
    if streak_of_ones:
        result += len(streak_of_ones)
    elif streak % 2 == 1:
        result += 1
    print(result)
    
            

