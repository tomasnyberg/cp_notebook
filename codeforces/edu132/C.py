import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def check_RBS(s):
    st = []
    for c in s:
        if c == '(':
            st.append(c)
        elif c == ')':
            if len(st) == 0:
                return False
            st.pop()
    return len(st) == 0

for RBS in lines[1:]:
    RBS = list(RBS)
    needed = len(RBS) // 2
    for c in RBS:
        if c == '(':
            needed -= 1
    lastleft = -1
    firstright = -1
    for i in range(len(RBS)):
        if RBS[i] == '?':
            if needed > 0:
                RBS[i] = '('
                needed -= 1
                lastleft = i
            else:
                if firstright == -1:
                    firstright = i
                RBS[i] = ')'
    if lastleft == -1 or firstright == -1:
        print("YES")
        continue
    RBS[lastleft], RBS[firstright] = RBS[firstright], RBS[lastleft]
    if check_RBS(RBS):
        print("NO")
    else:
        print("YES")
    

    
