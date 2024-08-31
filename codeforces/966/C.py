import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
# one-to-one correspondence

def check(string, template):
    if len(string) != len(template):
        return False
    mapped = {}
    mapped_to = set()
    for i, x in enumerate(string):
        if x not in mapped:
            if template[i] in mapped_to:
                return False
            mapped[x] = template[i]
            mapped_to.add(template[i])
        else:
            if mapped[x] != template[i]:
                return False
    return True


ii = 1
while ii < len(lines):
    n = int(lines[ii])
    ii+=1
    xs = list(map(int, lines[ii].split()))
    ii+=1
    m = int(lines[ii])
    ii+=1
    for _ in range(m):
        s = lines[ii]
        if check(s, xs):
            print("YES")
        else:
            print("NO")
        ii+=1