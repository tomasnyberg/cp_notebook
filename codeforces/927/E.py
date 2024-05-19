import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import random
sys.set_int_max_str_digits(5*10**5)
# TODO Remember to add int wrapping if using dict

def test(n):
    result = 0
    for i in range(n, 0,-1):
        result += 1
        stred = list(str(i))
        count = 0
        while stred and stred[-1] == '0':
            count += 1
            stred.pop()
        result += count
    return result

for line in lines[2::2]:
    result = 0
    to_add = 0
    for c in line:
        to_add *= 10
        to_add += int(c)
        result += to_add
    print(result)



        
