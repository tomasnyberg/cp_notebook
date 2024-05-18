# Returns an integer array Z, which for all its indices i answers the following:
# Starting at this index i of the string s, how many characters are the same as the prefix?
# So for example, for the string s="a a b a c a b a" and target = abac we would get
#                                  [1,4,0,1,0,3,0,1]
# Note how at index 2, we have a full match. So this could be used to find the max amount of times
# That you can match the target string.

# Example problem: https://codeforces.com/contest/1968/problem/G1 
def z_function(target, s):
    prefixed = target + s
    z = [0] * len(prefixed)
    left = right = 0
    for i in range(1, len(prefixed)):
        if i < right:
            z[i] = min(right - i, z[i-left])
        while i + z[i] < len(prefixed) and prefixed[i + z[i]] == prefixed[z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z[len(target):]

target = "abacaba"
s = "abacabacabacaba"
print(target)
print(s)
print(z_function(target, s))
