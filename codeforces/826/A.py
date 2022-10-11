import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    a, b = line.split(" ")
    axs = 0
    bxs = 0
    for c in a:
        if c =='X': axs += 1
    for c in b:
        if c =='X': bxs += 1
    if a[-1] != b[-1]:
        print(">" if a[-1] < b[-1] else "<")
    else:
        if axs == bxs:
            print("=")
        else:
            if a[-1] == 'S':
                print(">" if axs < bxs else "<")
            else:
                print("<" if axs < bxs else ">")
        
