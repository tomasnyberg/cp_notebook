import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    a = lines[i]
    b = lines[i+1]
    if a[0] == b[0]:
        print("YES")
        print(a[0] + "*")
        continue
    if a[-1] == b[-1]:
        print("YES")
        print("*" + a[-1])
        continue
    # Find every substring of a and b of length 2
    # If they are the same, print YES and the substring
    seen = set()
    for j in range(2, len(a) + 1):
        seen.add((a[j-2:j]))
    for j in range(2, len(b) + 1):
        if (b[j-2:j]) in seen:
            print("YES")
            print("*" + b[j-2:j] + "*")
            break
    else:
        print("NO")
    
