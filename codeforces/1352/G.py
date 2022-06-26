import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    n = int(line)
    taken = set()
    result = []
    curr = 1
    while len(taken) < n:
        result.append(curr)
        taken.add(curr)
        for i in range(max(1, curr - 4), min(n+1, curr + 5)):
            if i not in taken and i != curr and abs(i-curr) >= 2:
                curr = i
                break
    print(result) 