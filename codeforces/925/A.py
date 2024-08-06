import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict


def find_good(n):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                if i + j + k + 3 == n:
                    print(chr(i + 97) + chr(j + 97) + chr(k + 97))
                    return


for line in lines[1:]:
    n = int(line)
    find_good(n)
