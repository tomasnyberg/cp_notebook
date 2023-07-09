import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def calculate(x, iterations):
    result = 1
    orig_x = x
    for i in range(iterations - 1):
        result += x
        x *= orig_x
        if result > 10**18:
            return 10**18 + 500
    return result

# TODO we might want to first look at the small numbers since they grow super quickly

# print(calculate(2, 4))
# seen = set()
# def construct(k):
#     total = k+1
#     leaves = k
#     total += leaves * k
#     leaves *= k
#     if total > 10**18:
#         return
#     seen.add(total)
#     for _ in range(10000):
#         total += leaves * k
#         leaves *= k
#         if total > 10**18:
#             break
#         seen.add(total)

# for k in range(2, 10**4):
#     construct(k)
# print(len(seen))

for line in lines[1:]:
    n = int(line)
    for iterations in range(3, 30):
        low = 2
        high = 10**18
        while low < high:
            mid = (low + high) // 2
            if calculate(mid, iterations) < n:
                low = mid + 1
            else:
                high = mid
        if calculate(low, iterations) == n:
            print("YES")
            break
    else:
        print("NO")