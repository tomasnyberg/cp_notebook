import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def solve(line, first):
    if len(line) % 2:
        return (-1, -1)
    st = []
    colors = [-1]*len(line)
    line = list(enumerate(line))
    currcolor = 1
    check = '(' if first else ')'
    second_check = ')' if first else '('
    for i,c in line:
        if c == check:
            st.append((c,i))
        else:
            if st and st[-1][0] == check:
                _, idx = st.pop()
                colors[idx] = currcolor
                colors[i] = currcolor
            else:
                st.append((c,i))
    if len(st) != len(line):
        currcolor += 1
    line = st
    st = []
    for c, i in line:
        if c == second_check:
            st.append((c,i))
        else:
            if st and st[-1][0] == second_check:
                _, idx = st.pop()
                colors[idx] = currcolor
                colors[i] = currcolor
            else:
                st.append((c,i))
    if st:
        return (-1,-1)
    return (len(set(colors)), colors)

for line in lines[2::2]:
    a, c1 = solve(line, True)
    b, c2 = solve(line, False)
    if a == -1 and b == -1:
        print(-1)
        continue
    if a == -1:
        print(b)
        print(' '.join(map(str, c2)))
        continue
    if b == -1:
        print(a)
        print(' '.join(map(str, c1)))
        continue
    if a < b:
        print(a)
        print(' '.join(map(str, c1)))
    else:
        print(b)
        print(' '.join(map(str, c2)))
