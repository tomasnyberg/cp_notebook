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

# nums = [i for i in range(1, 202234)]
# random.shuffle(nums)
first = read_int()
first_thousand = [first]
positions = {first:1}
count = 1
while len(first_thousand) < 1000:
    # res = nums[count]
    res = query_clockwise(1) # UNCOMMENT
    count += 1
    if res in positions:
        print("!", count - positions[res])
        sys.exit(0)
    first_thousand.append(res)
    positions[res] = count

pos = 1001
while True:
    pos += 1000
    # res = nums[pos % len(nums)]
    res = query_clockwise(1000) #UNCOMMENT
    if res in positions:
        print("!", pos - positions[res])
        sys.exit(0)
    positions[res] = pos
