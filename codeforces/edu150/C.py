import sys
lines = list(map(str.strip, sys.stdin.readlines()))

values = {'A':1, 'B':10, 'C':100, 'D':1000, 'E':10000}

def calculate_score(line):
    biggest = ['A' for _ in range(len(line) + 1)]
    for i in range(len(line) - 1, -1, -1):
        biggest[i] = max(biggest[i + 1], line[i])
    result = 0
    for i in range(len(line)):
        if line[i] < biggest[i+1]:
            result -= values[line[i]]
            # print("-", values[line[i]])
        else:
            result += values[line[i]]
            # print("+", values[line[i]])
    return result
# s = "ABCEEEDCBA"
# s = list(s)
# for i in range(len(s)):
#     temp = s[i]
#     s[i] = 'E'
#     print(calculate_score(s))
#     s[i] = temp
# print(calculate_score(s))

for line in lines[1:]:
    lastseen = {}
    for i in range(len(line)):
        lastseen[line[i]] = i
    line = list(line)
    result = 0
    # Replace first with something
    for k in values:
        idx = -1
        for i in range(len(line)):
            if line[i] == k:
                line[i] = 'E'
                idx = i
                break
        else:
            continue
        # print(''.join(line), calculate_score(line))
        result = max(result, calculate_score(line))
        line[idx] = k
    # Replace last with something
    for k in values:
        if k not in lastseen:
            continue
        idx = lastseen[k]
        for y in values:
            if y == k: continue
            line[idx] = y
            result = max(result, calculate_score(line))
        line[idx] = k
    print(result)