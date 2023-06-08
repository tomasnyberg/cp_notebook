import sys
lines = list(map(str.strip, sys.stdin.readlines()))

target = "abacaba"

def attempt(s, startpoint):
    s = list(s)
    for j in range(len(target)):
        s[startpoint + j] = target[j]
    s = ''.join([x if x != "?" else "z" for x in s])
    count = 0
    for i in range(len(s) - 6):
        if s[i:i+7] == target:
            count += 1
    return ''.join(s) if count == 1 else False


for s in lines[2::2]:
    # i = position in s, j = position in target
    for startpoint in range(len(s) - 6):
        for j in range(len(target)):
            if s[startpoint + j] != target[j] and s[startpoint + j] != "?":
                break
        else:
            res = attempt(s, startpoint)
            if res:
                print("Yes")
                print(res)
                break
    else:
        print("No")



