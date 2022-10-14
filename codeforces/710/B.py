import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def replacefirstlast(s):
    result = 0
    for i in range(len(s)):
        if s[i] == '*':
            s[i] = 'x'
            result+=1
            break
    for i in range(len(s)-1,-1,-1):
        if s[i] =='*':
            s[i] = 'x'
            result +=1
            break
    return (s, result)

for i in range(1, len(lines), 2 ):
    n, k = map(int, lines[i].split(" "))
    s = list(lines[i+1])
    s, result = replacefirstlast(s)
    # print(s)
    for j in range(len(s)):
        if s[j] == 'x' and 'x' not in s[j+1:j+k]:
            for l in range(min(j + k, len(s)-1), j, -1):
                if s[l] == '*':
                    s[l] = 'x'
                    result += 1
                    break
    # print(s)
    print(result)
    # print("\n\n")
