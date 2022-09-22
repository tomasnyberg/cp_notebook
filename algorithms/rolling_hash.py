# Given an array of integers, returns hashvalues of a rolling window of size length
# In the form [hashvalue, startindex]
# Example: rolling([1,2,3,4,5,6,7,8,9], 3) returns [[38534, 0], [51417, 1], [64300, 2], [77183, 3], [90066, 4], [102949, 5], [115832, 6]]
# We have a very low chance of collision
# This is a very fast way to find all substrings of a string and subarrays of an array

def rolling(arr, length):
    if length == 0: return [[0, 0]]
    P = 113
    MOD = 10**9 + 7
    Pinv = pow(P, MOD - 2, MOD)
    result = []
    hashval, power = 0, 1
    for idx, x in enumerate(arr):
        hashval = (hashval + x * power) % MOD
        if idx < length - 1:
            power = (power * P) % MOD
        else:
            result.append([hashval, idx-length+1])
            hashval = (hashval - arr[idx - (length - 1)]) * Pinv % MOD
    return result

s = [1,2,3,4,5,6,7,8,9]
print(rolling(s, 3))