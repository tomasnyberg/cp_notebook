import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    s = list(line)
    V = ['a', 'e']
    C = ['b', 'c', 'd']
    result = []
    while s:
        rng = 3 if s[-1] in C else 2
        for _ in range(rng):
            result.append(s.pop())
        result.append('.')
    print(''.join(result[::-1][1:]))