import sys
lines = list(map(str.strip, sys.stdin.readlines()))

values = {'A':1, 'B':10, 'C':100, 'D':1000, 'E':10000}

for line in lines[1:]:
    line = list(line)
    for i in range(len(line)):
        if line[i] != 'E':
            line[i] = 'E'
            break
    biggest = ['A' for _ in range(len(line) + 1)]
    for i in range(len(line) - 1, -1, -1):
        biggest[i] = max(biggest[i + 1], line[i])
    print(''.join(line))
    result = 0
    for i in range(len(line)):
        if line[i] < biggest[i+1]:
            result -= values[line[i]]
            # print("-", values[line[i]])
        else:
            result += values[line[i]]
            # print("+", values[line[i]])
    print(result)