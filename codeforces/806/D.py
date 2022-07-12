import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(strs):
    seen = set(strs)
    for s in strs:
        found = False
        # if len(s) <= 1 # Might need to check for this if we get WA
        for i in range(1, len(s)):
            if s[:i] in seen and s[i:] in seen:
                found = True
                break
        print("1" if found else "0", end="")
    print()

# xs = ['abab', 'ab', 'abc', 'abacb', 'c']
# solve(xs)
i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    strs = []
    while n > 0:
        strs.append(lines[i])
        i += 1
        n -= 1
    solve(strs)