import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for s in lines[2::2]:
    result = 0
    i = 0
    while i < len(s):
        if s[i:i+5] == "mapie":
            result += 1
            i += 5
        elif s[i:i+3] == "map" or s[i:i+3] == "pie":
            result += 1
            i += 3
        else:
            i+=1
    print(result)
        

