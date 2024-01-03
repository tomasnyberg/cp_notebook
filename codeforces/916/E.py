import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 3):
    a = list(map(int, lines[ii+1].split()))
    b = list(map(int, lines[ii+2].split()))
    taken = set()
    zipped = list(enumerate(zip(a, b)))
    alicescores = []
    for i, (x, y) in zipped:
        alicescores.append((x-1+y, i, x-1))
    alicescores.sort()
    bobscores = []
    for i, (x, y) in zipped:
        bobscores.append((y-1+x, i, y-1))
    bobscores.sort()
    turn = 1
    result = 0
    # print(alicescores)
    # print(bobscores)
    while alicescores or bobscores:
        if turn:
            while alicescores and alicescores[-1][1] in taken:
                alicescores.pop()
            if not alicescores:
                continue
            score, i, toadd = alicescores.pop()
            # print("Alice takes", i, "with score", score)
            taken.add(i)
            result += toadd
        else:
            while bobscores and bobscores[-1][1] in taken:
                bobscores.pop()
            if not bobscores:
                continue
            score, i, toadd = bobscores.pop()
            # print("Bob takes", i, "with score", score)
            taken.add(i)
            result -= toadd
        turn = 1 - turn
    print(result)