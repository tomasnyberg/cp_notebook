import sys
lines = list(map(str.strip, sys.stdin.readlines()))


skips = {1: 1, 2: 18, 3: 252, 4: 3168, 5: 37512, 6: 427608}
skipped = {}
def get_count(x):
    if x == 0: return (0,0)
    res = 1
    power = 0
    for _ in range(x-1):
        res = res*9 + 9*10**power
        power += 1
    return (res, power)

# for i in range(10):
#     print(i, get_count(i))

for line in lines[1:]:
    n = (line)
    r, pow = get_count(len(n)-1)
    print(int(n) + (int(n[0])) * r)
