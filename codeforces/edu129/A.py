import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def play(a,b, initial):
    a = a.copy()
    b = b.copy()
    turn = initial
    last = 0
    while a or b:
        if turn % 2 == 0:
            if a and a[-1] > last:
                last = a.pop()
            else:
                return "Bob"
        else:
            if b and b[-1] > last:
                last = b.pop()
            else:
                return "Alice"
        turn += 1




for i in range(1, len(lines), 4):
    a = list(map(int, lines[i+1].split()))
    b = list(map(int, lines[i+3].split()))
    a.sort()
    b.sort()
    print(play(a,b,0))
    print(play(a,b,1))


