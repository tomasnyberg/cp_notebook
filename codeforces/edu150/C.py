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
    firstseen = {}
    for i in range(len(line)):
        if line[i] not in firstseen:
            firstseen[line[i]] = i
        lastseen[line[i]] = i
    line = list(line)
    result = 0
    # Replace first with something
    all_indices = set()
    all_indices.update(firstseen.values())
    # all_indices.update(lastseen.values())
    # print(all_indices)
    for idx in all_indices:
        temp = line[idx]
        for c in "ABCDE":
            line[idx] = c
            # print(''.join(line), calculate_score(line))
            result = max(result, calculate_score(line))
        line[idx] = temp
    print(result)