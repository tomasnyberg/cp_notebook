import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[1:]:
    n, k = map(int, line.split())
    if n == k:
        print(2*n)
        continue
    result = (k-1) * 2
    n -= (k-1)
    result += 2**n
    print(result)
