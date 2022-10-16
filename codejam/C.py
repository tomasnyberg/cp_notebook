import sys
lines = list(map(str.strip, sys.stdin.readlines()))
test = 1

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

def sliding_window(xs, size, result):
    count = 0
    left = 0
    right = 0
    while right < len(xs):
        count += (xs[right])
        if right - left >= size - 1:
            if all([x >= 0 for x in cum_sum(xs[left:right+1])]):
                # print("added", xs[left:right+1], count)
                result[0] += count
            count -= xs[left]
            left += 1
        right += 1

for line in lines[2::2]:
    result = [0]
    nums = list(map(int, line.split(" ")))
    for i in range(1, len(line)):
        sliding_window(nums, i, result)
    print("Case #{}: {}".format(test, result[0]))
    test+=1
