import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

test = 1
i = 1
while i < len(lines):
    rs, rh = map(int, lines[i].split(" "))
    i+=1
    n = int(lines[i])
    i+=1
    astones = []
    while n > 0:
        astones.append(list(map(int, lines[i].split(" "))))
        i+=1
        n-=1
    m = int(lines[i])
    i+=1
    bstones = []
    while m > 0:
        bstones.append(list(map(int, lines[i].split(" "))))
        i+=1
        m-=1
    astones = list(map(lambda x: math.sqrt(x[0]**2 + x[1]**2) - rs, astones))
    bstones = list(map(lambda x: math.sqrt(x[0]**2 + x[1]**2) - rs, bstones))
    # filter astones and bstones to not include ones furhter away from the origin than rh
    astones = list(filter(lambda x: x <= rh, astones))
    bstones = list(filter(lambda x: x <= rh, bstones))
    astones.sort()
    bstones.sort()
    ascore = 0
    bscore = 0
    if len(astones) == 0:
        bscore = len(bstones)
    elif len(bstones) == 0:
        ascore = len(astones)
    else:
        if astones[0] < bstones[0]:
            for j in range(len(astones)):
                if astones[j] < bstones[0]:
                    ascore+=1
                else:
                    break
        else:
            for j in range(len(bstones)):
                if bstones[j] < astones[0]:
                    bscore+=1
                else:
                    break
    print(f"Case #{test}: {ascore} {bscore}")
    test += 1
    # print(astones, bstones)


