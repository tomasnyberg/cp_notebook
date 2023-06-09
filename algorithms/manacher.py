# Manacher's algorithm for finding the longest palindromic substring in a string.
# Time complexity: O(n)
# Space complexity: O(n)

# Example problem: https://leetcode.com/problems/longest-palindromic-substring/
# Another, harder example: https://codeforces.com/contest/1326/problem/D2

def manacher(s):
    s = '#'.join('^{}$'.format(s))
    n = len(s)
    P = [0] * n
    C = R = 0
    for i in range(1, n-1):
        if R > i:
            i_mirror = 2*C - i  # i's mirror position in the previously calculated palindrome
            P[i] = min(R-i, P[i_mirror])  # Truncate P[i] at R if it overflows
        # Attempt to expand
        while s[i + 1 + P[i]] == s[i - 1 - P[i]]:
            P[i] += 1
        # Update C and R if i's palindrome expands past R
        if i + P[i] > R:
            C, R = i, i + P[i]
    max_length = max(P)
    center_index = P.index(max_length)
    return s[center_index - max_length:center_index + max_length].replace("#", "")

print(manacher("abcdfdcecba"))