import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def flattenamap(nums, m):
    for i in range(len(nums)):
        if nums[i] % m == 0 and nums[i] > m:
            curr = nums[i]
            multiplier = 0
            while curr % m == 0:
                curr //= m
                multiplier += 1
            nums[i] = [m**multiplier, curr]
        elif nums[i] % m == 0 and nums[i] == m:
            nums[i] = [m, 1]

    return nums

def compareflats(xs, ys):
    a = 0
    b = 0
    while a < len(xs) and b < len(ys):
        # print(a, b, xs[a], ys[b])
        # If both of them hit an array, check like this
        if type(ys[b]) == type(ys) and type(xs[a]) == type(xs): # If b is at an array as well 
            # If they have an equal amount of elements, just move both ahead
            if ys[b][1] != xs[a][1]: return False
            if ys[b][0] == xs[a][0]:
                a += 1
                b += 1
                continue
            if ys[b][0] > xs[a][0]:
                ys[b][0] -= xs[a][0]
                a+=1
            else:
                xs[a][0] -= ys[b][0]
                b += 1
            continue
        # xs is an array but ys isn't
        if type(xs[a]) == type(xs):
            if ys[b] != xs[a][1]: return False
            xs[a][0] -= 1
            b+=1
            if xs[a][0] == 0:
                a += 1
            continue
        if type(ys[b]) == type(xs):
            if ys[b][1] != xs[a]: return False
            ys[b][0] -= 1
            a+=1
            if ys[b][0] == 0:
                b += 1           
            continue
        #Neither of them are at an array
        if xs[a] != ys[b]:
            return False
        a += 1
        b += 1
        
    return a == len(xs) and b == len(ys)

for i in range(1, len(lines), 4):
    n, m = map(int, lines[i].split(" "))
    a_nums = list(map(int, lines[i+1].split(" ")))
    b_nums = list(map(int, lines[i+3].split(" ")))
    aflat = flattenamap(a_nums, m)
    bflat = flattenamap(b_nums, m)
    # print(aflat)
    # print(bflat)
    print("YES" if compareflats(aflat, bflat) else "NO")
