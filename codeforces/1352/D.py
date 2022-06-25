import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(2, len(lines), 2):
    candies = list(map(int, lines[i].split(" ")))
    alice = 0
    bob = len(candies) - 1
    boblast = 0
    alicelast = 0
    moves = 0

    a = 0
    b = 0
    while alice <= bob:
        while alicelast <= boblast and alice <= bob:
            if alicelast == 0:
                moves += 1
            alicelast += candies[alice]
            a += candies[alice]
            alice += 1
            if alicelast > boblast:
                boblast = 0
        while boblast <= alicelast and alice <= bob:
            if boblast == 0:
                moves += 1
            boblast += candies[bob]
            b += candies[bob]
            bob -= 1
            if boblast > alicelast:
                alicelast = 0
    print(moves, a, b)