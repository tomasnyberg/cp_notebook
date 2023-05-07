import sys
lines = list(map(str.strip, sys.stdin.readlines()))

nums = list(map(int, lines[1].split(" ")))

def check(xs):
    running = 0
    for x in xs:
        running += x
        if running < 0:
            return False
    return True
xs = [x if x >= 0 else 0 for x in nums]
negatives = [(x, i) for i, x in enumerate(nums) if x < 0]
negatives.sort(key=lambda x: (-x[0], -x[1]))
result = len([x for x in nums if x >= 0])
for x, i in negatives:
    xs[i] = x
    if check(xs):
        # print("Took", x, i)
        result += 1
    else:
        xs[i] = 0
print(result)



