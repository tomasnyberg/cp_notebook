import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import random
import math

def makeMove(x):
    if x %2 == 1:
        return 1
    else:
        if x <= 10 or (x // 2) % 2 == 1:
            return x // 2
        else:
            return 1
        
for line in lines[1:]:
    x = int(line)
    result = 0
    while x > 0:
        amove = makeMove(x)
        # print(amove, " taken by Mr. Chanek")
        result += amove
        x-=amove
        bmove = makeMove(x)
        # print(bmove, " taken by other guy")
        x-=makeMove(x)
    print(result)