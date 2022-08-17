import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    streak = 0
    firstquestion = -1
    i = 1
    even = -1 # Should our ones be on even indexes?
    while i < len(line):
        if even == -1:
            even = i % 2 == 0 and line[i] == '1'
            if line[i] == '?': even = -1
        if i % 2 == 0:
            if (even and line[i] == '0') or (not even and line[i] == '1'):
                print("streak broken at", i, "got to", streak)
                even = not even
                streak = 0
        if i % 2 == 1:
            if (even and line[i] == '1') or (not even and line[i] == '0'):
                print("streak broken at", i, "got to", streak) 
                even = not even
                streak = 0
        streak += 1
        i+= 1