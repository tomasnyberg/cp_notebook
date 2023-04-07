import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def makeMove(x):
    return 1 if not (x%2==0 and (x <= 8 or (x // 2) % 2 == 1)) else x // 2
        
for line in lines[1:]:
    x = int(line)
    result = 0
    while x > 0:
        amove = makeMove(x)
        result += amove
        x-=amove
        x-=makeMove(x)
    print(result)