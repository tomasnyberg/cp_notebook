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

for s in lines[1:]:
    s = list(s)
    last = {}
    first = {}
    for i in range(len(s)):
        if not s[i] in first:
            first[s[i]] = i
        last[s[i]] = i
    indices = set(last.values()) | set(first.values())
    result = -10**25
    for x in ['A', 'B', 'C', 'D', 'E']:
        for idx in indices:
            temp = s[idx]
            s[idx] = x
            result = max(result, calculate_score(s))
            s[idx] = temp
    print(result)