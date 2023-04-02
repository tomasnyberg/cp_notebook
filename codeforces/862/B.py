import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    line = list(line)
    smallest = min(line)
    occurrences = [i for i in range(len(line)) if line[i] == smallest]
    line.pop(occurrences[-1])
    print(smallest + ''.join(line))