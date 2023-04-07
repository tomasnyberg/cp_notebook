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
    if k == 0 or all(c == '1' for c in s) or all(c == '0' for c in s): # If we can't change the string, just print its score
        print(f(s))
        continue
    # We can see how many swaps is needed to swap something to the front and to the back with
    # split[0] and split[-1] respectively.
    split = s.split("1")
    score = f(s)
    if s[-1] != '1' and len(split[-1]) <= k:
        if score == 10: # We have literally only one 1 in the string and it is at the front
            print(1)
            continue
        score -= 10
        k-= len(split[-1])
    if s[0] != '1' and len(split[0]) <= k and score != 1: # Last check is needed to not take a 1 out of the perfect last spot
        score -= 1
    print(score)