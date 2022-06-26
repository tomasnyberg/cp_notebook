import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    # special = []
    # for i in range(1, min(n+1, 5)):
    #     special.append(i)
    # for i in range(n, max(n-4, 0), -1):
    #     special.append(i)
    possible_matches = {i:[] for i in range(1, n+1)}
    for x in possible_matches:
        for i in range(max(1, x - 4), min(n+1, x + 5)):
            if i != x and abs(i-x) >= 2:
                possible_matches[x].append(i)
    taken = set()
    result = []
    curr = 1
    while len(taken) < n:
        result.append(curr)
        taken.add(curr)
        for pos_match in possible_matches[curr]:
            if pos_match not in taken:
                curr = pos_match
                break
    print(result) 