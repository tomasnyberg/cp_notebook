import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    streak = 0
    firstquestion = -1
    i = 0
    result = 0
    even = -1 # Should our ones be on even indexes?
    while i < len(line):
        curr = line[i]
        if even == -1:
            even = i % 2 == 0 and curr == '1'
            if curr == '?': even = -1
        if curr != '?':
            curr = int(curr)
            if (even and curr == i%2) or (not even and curr == (i+1)%2):
                even = not even
                result += (streak*(streak+1))//2
                streak = 0
        streak += 1
        i+= 1
    result += (streak*(streak+1))//2
    print(result)