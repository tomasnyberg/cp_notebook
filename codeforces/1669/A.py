import sys
lines = list(map(str.strip, sys.stdin.readlines()))


# For Division 1: 1900≤rating
# For Division 2: 1600≤rating≤1899
# For Division 3: 1400≤rating≤1599
# For Division 4:  rating≤1399

for line in lines[1:]:
    x = int(line)
    if x >= 1900:
        print("Division 1")
    elif x >= 1600:
        print("Division 2")
    elif x >= 1400:
        print("Division 3")
    else:
        print("Division 4")