import sys, re
lines = list(map(str.strip, sys.stdin.readlines()))


def eval_paren(line, start, end, evaluated):
    result = 0
    i = start
    operator = None
    while i < end:
        if line[i] == ' ':
            i += 1
            continue
        if line[i] == '(':
            if operator == '+':
                result += evaluated[i]
            elif operator == '*':
                result *= evaluated[i]
            i+=1
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
    st = []
    evaluated = {}
    for i in range(len(line)):
        if line[i] == '(':
            st.append(i)
        elif line[i] == ')':
            start = st.pop()
            evaluated[start] = eval_paren(line, start+1, i+1, evaluated)
    result += eval_paren(line, 0, len(line), evaluated)
    print(line)
    print(evaluated)

print(result)