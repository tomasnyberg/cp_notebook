import sys
lines = list(map(str.strip, sys.stdin.readlines()))

fbstring = ""
for i in range(100000):
    if i % 3 == 0:
        fbstring += "F"
    if i % 5 == 0:
        fbstring += "B"


for line in lines[2::2]:
    if line in fbstring:
        print("YES")
    else:
        print("NO")