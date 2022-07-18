import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def all_two_or_three(others):
    seen = {}
    for i in range(2, 4):
        for idx, other in enumerate(others):
            left = 0
            right = i
            while right <= len(other):
                curr = other[left:right]
                seen[curr] = [left + 1, right, idx + 1]
                left +=1
                right +=1
    return seen

a = 2
while a < len(lines):
    n, l = map(int, lines[a].split(" "))
    a+=1
    others = []
    while n >= 0:
        others.append(lines[a])
        n-=1
        a+=1
    a+=1
    friend = others.pop()
    seen = all_two_or_three(others)
    dp = []
    for i in range(len(friend)):
        dp.append([])
    for i in range(len(dp)-1):
        if not (i == 0 or (i >= 2 and len(dp[i-2]) > 0) or (i >= 3 and len(dp[i-3]) > 0)): continue
        if friend[i:i+2] in seen:
            dp[i].append(seen[friend[i:i+2]])
        if i == len(dp) - 1: break # Skip len 3 ones
        if friend[i:i+3] in seen:
            dp[i].append(seen[friend[i:i+3]])
    print(seen[friend[0:2]])
    print(others)
    print(friend)
    print(dp)