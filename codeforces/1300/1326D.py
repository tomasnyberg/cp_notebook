import sys
lines = list(map(str.strip, sys.stdin.readlines()))
from functools import lru_cache

def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
        return
    N = 2*N+1    # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition
    R = 2     # centerRightPosition
    i = 0    # currentRightPosition
    iMirror = 0     # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1
    for i in range(2,N):
        iMirror = 2*C-i
        L[i] = 0
        diff = R - i
        if diff > 0:
            L[i] = min(L[iMirror], diff)
        try:
            while ((i+L[i]) < N and (i-L[i]) > 0) and \
                    (((i+L[i]+1) % 2 == 0) or \
                    (text[(i+L[i]+1)//2] == text[(i-L[i]-1)//2])):
                L[i]+=1
        except Exception as e:
            pass
        if L[i] > maxLPSLength:        # Track maxLPSLength
            maxLPSLength = L[i]
            maxLPSCenterPosition = i
        if i + L[i] > R:
            C = i
            R = i + L[i]
    return L

def expand(s, i, j):
    same = i == j
    a = ""
    b = ""
    while i >= 0 and j < len(s) and s[i] == s[j]:
        a += s[i]
        b += s[j]
        i -= 1
        j += 1
    a = a[1:] if same else a
    return a + b


for s in lines[1:]:
    start = ""
    end = ""
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            break
        start += s[i]
        end += s[j]
        i += 1
        j -= 1
    end = end[::-1]
    middle = findLongestPalindromicString(s[i:j+1])
    longest = [-1,-1]
    zeroes = 1
    for ii in range(1, len(middle)):
        if middle[i] == ii or middle[ii] + ii == len(middle) - 1:
            longest = max(longest, [middle[ii], ii - zeroes])
        if middle[ii] == 0:
            zeroes += 1
    candidates = []
    idx = longest[1]
    for a, b in [(idx, idx), (idx, idx+1), (idx-1, idx)]:
        candidates.append(expand(s[i:j+1], a, b))
    middle = max(candidates, key=len)
    print(start + middle + end)