import sys
from collections import deque
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    n = int(lines[ii])
    n*=2
    trump = lines[ii+1]
    def beats(a, b):
        if a[1] == trump and b[1] == trump:
            return a[0] > b[0]
        if a[1] == trump:
            return True
        if a[1] != b[1]:
            return False
        return a[0] > b[0]
    cards = lines[ii+2].split()
    orig_cards = lines[ii+2].split()
    cards = [(10**9 if c[1] == trump else 0, c[0], c[1], c) for c in cards]
    cards.sort()
    taken = [False]*n
    played = []
    for i in range(n):
        if taken[i]:
            continue
        for j in range(i+1, n):
            if taken[j]:
                continue
            # print(cards[i][3], cards[j][3], beats(cards[j][3], cards[i][3]))
            if beats(cards[j][3], cards[i][3]):
                taken[i] = True
                taken[j] = True
                played.append((cards[i][3], cards[j][3]))
                break
    # print(taken)
    if all(taken):
        for xs in played:
            print(*xs)
    else:
        print("IMPOSSIBLE")