import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def shift_arr(xs, steps, i):
    first_half = xs[:i]
    other_half = xs[i:]
    new_first_half = [-1] * len(first_half)
    for i in range(len(first_half)):
        new_index = i - steps
        if new_index < 0:
            new_index = len(first_half) + new_index
        new_first_half[new_index] = first_half[i]
    return new_first_half + other_half

def find_amount_to_shift(xs, i):
    curr_index = xs.index(i) + 1
    amount_to_shift = curr_index if curr_index != i else 0
    return amount_to_shift

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    result = []
    for i in range(len(nums), 1, -1):
        curr_index = nums.index(i) + 1 # Index + 1of the number we want to get to the right place
        amount_to_shift = curr_index if curr_index != i else 0
        nums = shift_arr(nums,amount_to_shift,i)
        result.append(amount_to_shift)
    result.append(0)
    result.reverse()
    for x in result:
        print(x, end= " ")
    print()
    