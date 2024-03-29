import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def score_arr(s):
    inarow = 0
    score = [0]*len(s)
    for idx, c in enumerate(s):
        if c == 'W':
            score[idx] = 2 if inarow >= 1 else 1
            inarow+=1
        else:
            inarow = 0
    return score

for i in range(1, len(lines),2):
    n, k = map(int, lines[i].split(" "))
    s = lines[i+1]
    wins = sum([1 if c == 'W' else 0 for c in s])
    result = sum(score_arr(s))
    if wins == 0:
        if k==0:
            print(result)
            continue
        print(min(k, len(s))*2 - 1)
        continue
    split = s.split("W")
    lentofirstandlast = len(split[0]) + len(split[-1])
    split = list(filter(lambda x: len(x) > 0, split[1:][:-1]))
    split.sort(key=lambda x: -len(x))
    while split:
        if k < len(split[-1]):
            result += k*2 
            k = 0
            break
        result += len(split[-1])*2+1
        k-= len(split[-1])
        split.pop()
    result += min(k, lentofirstandlast) * 2 
    print(result)
