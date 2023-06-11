import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    if len(line) % 2:
        print(-1)
        continue
    st = []
    colors = [-1]*len(line)
    line = list(enumerate(line))
    for i,c in line:
        if c == '(':
            st.append((c,i))
        else:
            if st and st[-1][0] == '(':
                _, idx = st.pop()
                colors[idx] = 1
                colors[i] = 1
            else:
                st.append((c,i))
    for i in range(len(colors)):
        if colors[i] == -1:
            colors[i] = 2 if len(st) < len(line) else 1
    print(len(set(colors)))
    print(*colors)