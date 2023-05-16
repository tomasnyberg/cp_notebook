# Description: Bit manipulation algorithms

# Generate the sum of XOR over all subsequences of an array
def xorSum(arr, n):
    bits = 0
    for i in range(n):
        bits |= arr[i]
    ans = bits * pow(2, n-1)
    ans %= 1000000007
    return ans