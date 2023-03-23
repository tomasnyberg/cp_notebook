import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def count_positive_sum_subarrays(xs):
    res = 0
    for i in range(len(xs)):
        for j in range(i, len(xs)):
            if sum(xs[i:j+1]) > 0:
                res += 1
    return res

# for j in range(31):
#     xs = [-1] * j + [100]*(30-j)
#     print(count_positive_sum_subarrays(xs), j) 
#     res = count_positive_sum_subarrays(xs)


def find(k):
    for i in range(1, 100):
        if (i*(i+1))//2 == k:
            return i
        elif (i*(i+1))//2 > k:
            return i-1
        
def solve(n, k):
    start = [1000]*n
    for i in range(n + 1):
        if count_positive_sum_subarrays(start) - k <= 0:
            break
        start[i] = -32
    to_get = -(count_positive_sum_subarrays(start) - k)
    idx = 0
    while to_get > 0:
        amount = find(to_get)
        to_get -= amount*(amount+1)//2
        while amount:
            start[idx] = 1
            idx += 1
            amount -= 1
        idx += 1
    # print("Our n, k are", n, k)
    print(*start)
    # print(count_positive_sum_subarrays(start))



# import random
# for _ in range(100):
#     n = random.randint(1, 30)
#     k = random.randint(0, n*(n+1)//2)
#     solve(n, k)

# solve(30, 29*(30)//2+29)

for line in lines[1:]:
    n, k = map(int, line.split())
    solve(n, k)