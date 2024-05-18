import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

def max_score(permutation, score_arr, start, k):
    result = 0
    running = 0
    pos = start
    seen = set()
    for remaining in range(k, 0, -1):
        if pos in seen:
            break
        result = max(remaining * score_arr[pos] + running, result)
        running += score_arr[pos]
        seen.add(pos)
        pos = permutation[pos]
    return result

for ii in range(1, len(lines), 3):
    n, k, a, b = map(int, lines[ii].split())
    permutation = list(map(int, lines[ii+1].split()))
    score_arr = list(map(int, lines[ii+2].split()))
    for i in range(len(permutation)):
        permutation[i] -= 1
    ascore = max_score(permutation, score_arr, a-1, k)
    bscore = max_score(permutation, score_arr, b-1, k)
    if ascore == bscore:
        print("Draw")
        continue
    print("Bodya" if bscore < ascore else "Sasha")