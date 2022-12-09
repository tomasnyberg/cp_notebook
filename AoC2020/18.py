import sys
lines = list(map(str.strip, sys.stdin.readlines()))

result = 0
def eval_paren(line, start, end):
    result = 0
    i = start
    operator = None
    while i < end:
        if line[i] == ' ':
            i += 1
            continue
        if line[i] == '(':
            opened = 0
            # Find the closing parenthesis
            otherend = -1
            for j in range(i, end):
                if line[j] == '(':
                    opened += 1
                elif line[j] == ')':
                    opened -= 1
                    if opened == 0:
                        otherend = j + 1
                        break
            res = eval_paren(line, i+1, otherend)
            if operator:
                if operator == '+':
                    result += res
                elif operator == '*':
                    result *= res
            else:
                result = res
            i = otherend
            continue
        if line[i] in ['+', '*']:
            operator = line[i]
        if line[i].isdigit():
            if operator:
                if operator == '+':
                    result += int(line[i])
                elif operator == '*':
                    result *= int(line[i])
            else:
                result = int(line[i])
        i += 1
    # print("eval paren", line[start:end], result, start, end)
    return result
result = 0
for line in lines:
    result += eval_paren(line, 0, len(line))

print(result)