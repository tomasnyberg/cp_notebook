def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

def cumsum2d(arr):
    result = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[0])):
            sum += arr[i][j]
            result[i][j] = sum + (result[i-1][j] if i > 0 else 0)
    return result

# Example of where you can use 2d prefixsum:
# https://codeforces.com/contest/1722/problem/E
# Explanation of how they work
# https://usaco.guide/silver/more-prefix-sums?lang=cpp#2d-prefix-sums
# Note that how you calculate the sums is not really trivial, you take the sum of 
# bottom right and top left and then subtract the sum of top right and bottom left.