import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def flattenamap(nums, m):
    for i in range(len(nums)):
        if nums[i] % m == 0 and nums[i] > m:
            nums[i] = [nums[i]//m, m]
    return nums

def compareflats(xs, ys):
    a = 0
    b = 0
    while a < len(xs) and b < len(ys):
        # If both of them hit an array, check like this
        if type(ys[b]) == type(ys) and type(xs[a]) == type(xs): # If b is at an array as well 
            # If they have an equal amount of elements, just move both ahead
            if ys[b][0] == xs[a][0]:
                a += 1
                b += 1
            if ys[b][0] > xs[a][0]:
                ys[b][0] -= xs[a][0]
                a+=1
            else:
                xs[a][0] -= ys[b][0]
                b += 1
        # xs is an array but ys isn't
        if type(xs[a]) == type(xs):
            if ys[b] != m: return False
            xs[a][0] -= 1
            if xs[a][0] == 0:
                a += 1
        if type(ys[b]) == type(xs):
            if xs[a] != m: return False
            xs[a][0] -= 1
            if xs[a][0] == 0:
                a += 1           
                        
    return a == len(xs) and b == len(ys)

for i in range(1, len(lines), 4):
    n, m = map(int, lines[i].split(" "))
    a_nums = list(map(int, lines[i+1].split(" ")))
    b_nums = list(map(int, lines[i+3].split(" ")))
    aflat = flattenamap(a_nums, m)
    bflat = flattenamap(b_nums, m)
    print(aflat)
    print(bflat)
    print("YES" if compareflats(aflat, bflat) else "NO")
