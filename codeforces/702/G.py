import sys
lines = list(map(str.strip, sys.stdin.readlines()))

# Modified cum_sum so that we only count when we actually increase our score
def cum_sum(nums):
    prev_pos = 0
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        if curr >= prev_pos:
            result[idx] = curr
            prev_pos = curr
        else:
            result[idx] = prev_pos
    return result

# Binary search with given start values, we assume we get a good value
# in as needed, we need to actually calculate this beforehand in the solve method
def bs(left, right, CS, needed):
    low = left
    high = right
    while low < high:
        mid = (low + high) >> 1
        # These might need to be flipped
        if CS[mid] < needed:
            low = mid + 1
        else:
            high = mid
    return low

def solve(target, nums, CS, pointer):
    initial_score = nums[pointer]
    spins = 0
    if initial_score >= target:
        return [pointer, 0]
    needed = target - initial_score
    # Spin the disc around to the right, get all the numbers there
    right_search = bs(pointer, len(nums), CS, needed + CS[pointer])
    left_gained = 0
    # We gained every element from our current start to the end
    if right_search == len(nums):
        left_gained += CS[-1] - CS[pointer] 
    else:
        left_gained += CS[right_search] - CS[pointer]
    spins += right_search - pointer
    needed -= left_gained
    if needed <= 0: # If we got everything we needed from just the right side, we're good.
        return [right_search, spins]
    left_search = bs(0, pointer, CS, needed) # Don't add anything to needed since we are searching from the start
    left_gained = CS[left_search]
    needed -= left_gained
    # print(needed)
    return [pointer,spins]


i = 1
while i < len(lines):
    n, m = map(int, lines[i].split(" "))
    i+=1
    nums = list(map(int, lines[i].split(" ")))
    i+= 1
    m_nums = list(map(int, lines[i].split(" ")))
    i+=1
    pointer = 0
    CS = cum_sum(nums)
    for x in m_nums:
        ptr, spins = solve(x, nums, CS, pointer)
        print(spins, end=" ")
        pointer = ptr
    print()
