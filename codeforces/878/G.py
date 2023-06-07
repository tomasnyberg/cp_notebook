import sys
import math

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

first = read_int()
curr = -1
result = 0
while curr != first:
    curr = query_clockwise(1)
    result += 1
print_ans(result)