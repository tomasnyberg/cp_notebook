import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    replaced = {}
    linecopy = line[:]
    line = list(line)
    for start in ['0', '1']:
        replaced[line[0]] = start
        line[0] = start
        for i in range(1, len(line)):
            if line[i] in replaced:
                line[i] = replaced[line[i]]
            else:
                li = line[i]
                line[i] = '0' if line[i-1] == '1' else '1'
                replaced[li] = line[i]
        # print(line, linecopy)
        # print(replaced)
        for i in range(1, len(line)):
            if line[i] == line[i-1]:
                break
        else:
            print("YES")
            break
        line = list(linecopy)
        replaced = {}
    else:
        print("NO")
    