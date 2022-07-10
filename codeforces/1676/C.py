import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1

def cost_to_change(a, b):
    result = 0
    for x, y in zip(a, b):
        diff = abs(ord(x) - ord(y))
        result += diff
    return result

while i < len(lines):
    words = []
    n, l = map(int, lines[i].split(" "))
    i+=1
    while n > 0:
        words.append(lines[i])
        i+=1
        n-=1
    result = 100000000000000000000
    for c in range(len(words)):
        for d in range(c + 1, len(words)):
            result = min(cost_to_change(words[c], words[d]), result)
    print(result)
