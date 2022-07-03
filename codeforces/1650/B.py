import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def f(x, a):
    return x // a + (x % a)


for line in lines[1:]:
    l, r, a = map(int, line.split(" "))
    if r < a:
        print(r)
        continue
    biggest_num = f(r, a) # Case 1: Straight up f
    other_best = (r//a - 1) + (a-1)
    other_best_x = (r//a - 1)*a + (a-1)
    if other_best_x >= l:
        print(max(biggest_num, other_best))
    else:
        print(biggest_num)