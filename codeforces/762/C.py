import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, s = line.split(" ")
    i = len(a) - 1
    j = len(s) - 1
    result = ""
    bad = False
    while j >= 0:
        x = int(a[i]) if i >= 0 else 0
        y = int(s[j])
        if x <= y:
            result+=str(y-x)
            i-=1
            j-=1
        else:
            if j == 0 or s[j-1] != '1':
                bad = True
                break
            y = int(s[j-1:j+1])
            if y > 18 or y - x >= 10:
                bad = True
                break
            result += str(y-x)
            j-=2
            i-=1
    if bad or i >= 0:
        print(-1)
        continue
    print(int(result[::-1]))
