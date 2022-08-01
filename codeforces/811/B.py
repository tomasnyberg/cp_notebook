import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    occurrences = {}
    for idx, x in enumerate(nums):
        if x not in occurrences:
            occurrences[x] = [idx + 1]
        elif len(occurrences[x]) == 2:
            occurrences[x][0] = occurrences[x][1]
            occurrences[x][1] = idx + 1
        else:
            occurrences[x].append(idx+1)
    most_to_remove = 0
    for key in occurrences:
        if len(occurrences[key]) == 1: continue
        most_to_remove = max(most_to_remove, occurrences[key][0])
    print(most_to_remove)