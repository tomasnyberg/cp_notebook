import sys
import math
import random

def read_int():
    return int(sys.stdin.readline())

def print_ans(ans):
    print("!", ans)
    sys.stdout.flush()

def query_clockwise(x):
    print("+", x)
    sys.stdout.flush()
    return read_int()

def query_counter_clockwise(x):
    print("-", x)
    sys.stdout.flush()
    return read_int()

nums = [i for i in range(1, 10**6)]
random.shuffle(nums)

first_thousand = []
first_thousand_set = set()
at_least = read_int()
at_most = 10**6
first_thousand.append(at_least)
first_thousand_set.add(at_least)
count = 0
while len(first_thousand) < 1000:
    count += 1
    res = query_clockwise(1)
    if res in first_thousand_set:
        print("!", count)
        sys.exit(0)
    at_least = max(at_least, res)
    first_thousand.append(res)
    first_thousand_set.add(res)
query_counter_clockwise(500)

queries = 1000
while True:
    # res = query_clockwise(at_least) # uncomment 
    # query_counter_clockwise(at_least)
    res = nums[(500 + at_least - 1) % len(nums)]
    at_least = max(at_least, res)
    queries += 2
    if res in first_thousand_set:
        print(res, at_least)
        idx = first_thousand.index(res)
        if idx < 500:
            print_ans(at_least + 500 - idx)
        else:
            print_ans(at_least - (idx - 500))
        print("queries:", queries)
        break
    at_least += 500
