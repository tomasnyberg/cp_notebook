import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def binary_search(a, b, longest):
    def check(x):
        return x * 2**longest <= b
    low = a
    high = b
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            low = mid + 1
        else:
            high = mid
    return low - 1

def binary_search_3(a, b, longest):
    def check(x):
        return x * 3 * 2**(longest-1) <= b
    low = a
    high = b
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            low = mid + 1
        else:
            high = mid
    return low - 1


for line in lines[1:]:
    a, b = map(int, line.split())
    longest = 0
    x = a
    while x <= b:
        longest += 1
        x *= 2
    longest -= 1
    if longest == 0:
        print(1, b-a +1)
        continue
    # print(a, " can at most be multipled by 2^", longest)
    # print(a * 2**longest, longest)
    res = binary_search(a, b, longest)
    res2 = binary_search_3(a, b, longest)
    # print("2s and threes", res, res2)
    only_twos = res - a + 1
    one_three = res2 - a + 1
    # print("threes:", one_three)
    # print(only_twos, one_three)
    print(longest+1, only_twos + one_three*(longest))
    

     