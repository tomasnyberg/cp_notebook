import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def f(s):
    total = 0
    for i in range(2, len(s)+1):
        total += int(s[i-2:i])
    return total

def move_back_cost(s):
    for i in range(len(s)-1 ,-1, -1):
        if s[i] == '1':
            return(len(s) - i - 1)

def move_front_cost(s):
    for i in range(0, len(s)):
        if s[i] == '1':
            return i

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    s = lines[i+1]
    if k == 0 or all(c == '1' for c in s) or all(c == '0' for c in s): # If we can't change the string, just print its score
        print(f(s))
        continue
    need_to_move_to_back = s[-1] != '1'
    need_to_move_to_front = s[0] != '1'
    cost_to_move_to_back = move_back_cost(s)
    cost_to_move_to_front = move_front_cost(s)
    score = f(s)
    if need_to_move_to_back and cost_to_move_to_back <= k:
        if score == 10: # We have literally only one 1 in the string and it is at the front
            print(1)
            continue
        score -= 10
        k-=cost_to_move_to_back
    if need_to_move_to_front and cost_to_move_to_front <= k and score != 1:
        score -= 1
    print(score)