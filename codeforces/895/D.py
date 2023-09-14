import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

def f(x):
    return x*(x+1)//2
for line in lines[1:]:
    n, x, y = map(int, line.split())
    
    
    
    
