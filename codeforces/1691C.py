import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def f(s):
    total = 0
    for i in range(2, len(s)+1):
        total += int(s[i-2:i])
    return total

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    s = lines[i+1]
    if k == 0: # If we can't change the string, just print its score
        print(f(s))
        continue    