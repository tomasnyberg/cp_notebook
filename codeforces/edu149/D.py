import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    if len(line) % 2:
        print(-1)
        continue
    st = []
    colors = [-1]*len(line)
    line = list(enumerate(line))
    currcolor = 1
    for i,c in line:
        if c == '(':
            st.append((c,i))
        else:
            if st and st[-1][0] == '(':
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
        if c == ')':
            st.append((c,i))
        else:
            if st and st[-1][0] == ')':
                _, idx = st.pop()
                colors[idx] = currcolor
                colors[i] = currcolor
            else:
                st.append((c,i))
    if st:
        print(-1)
        continue
    print(len(set(colors)))
    print(*colors)