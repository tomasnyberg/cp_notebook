import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(dominoes, one, two, prevlen): # call this recursively
    undecided = []
    for a, b in dominoes:
        # print(one, two, [a, b])
        if a == b:
            print("NO")
            return
        if len(one) == 0 and len(two) == 0:
            one.add(a)
            one.add(b)
            continue
        
        if (a not in one and a not in two) and (b not in one and b not in two):
            undecided.append([a,b])
            continue
        
        if a in one or b in one:
            if a in two or b in two:
                print("NO")
                return
            else:
                two.add(a)
                two.add(b)
                continue
        if a in two or b in two:
            if a in one or b in one:
                print("NO")
                continue
            else:
                one.add(a)
                one.add(b)
                continue
    if len(undecided) == 0:
        print("YES")
        return
    if len(undecided) == prevlen:
        solve(undecided, set(), set(), len(undecided))
    else:
        solve(undecided, one, two, len(undecided))
            

i = 1
while i < len(lines):
    n = int(lines[i])
    i+=1
    dominoes = []
    while n > 0:
        a, b = map(int, lines[i].split(" "))
        dominoes.append([a,b])
        i+=1
        n-=1
    solve(dominoes, set(), set(), len(dominoes))
    

