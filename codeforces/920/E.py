import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    h, w, y1, x1, y2, x2 = map(int, line.split())
    diff = y2 - y1
    if diff <= 0:
        print("Draw")
        continue
    winner = 1 if diff % 2 == 1 else 2 # Alice can win if diff is odd, otherwise Bob wins
    winnermap = {1: "Alice", 2: "Bob"}
    alicesteps = diff // 2
    bobsteps = (diff - 1) // 2
    direction = 0 # 1 = right, -1 = left
    if winner == 1:
        direction = 1 if x2 >= x1 else -1 
        bobfurthest = x2 + bobsteps * direction
        alicefurthest = x1 + alicesteps * direction
    else:
        direction = 1 if x2 <= x1 else -1
        bobfurthest = x2 + bobsteps * direction
        alicefurthest = x1 + alicesteps * direction
    if direction == 1:
        bobfurthest = min(bobfurthest, w)
        alicefurthest = min(alicefurthest, w)
    else:
        bobfurthest = max(bobfurthest, 1)
        alicefurthest = max(alicefurthest, 1)
    print(winnermap[winner] if abs(bobfurthest - alicefurthest) <= 1 else "Draw")
    