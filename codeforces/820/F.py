import sys
lines = list(map(str.strip, sys.stdin.readlines()))

def subsums(s, w):
    left = 0
    right = 0
    curr = ""
    possiblemods = {}
    result = []
    while right < len(s):
        curr += s[right]
        if len(curr) == w:
            num = int(curr) % 9
            if num not in possiblemods: possiblemods[num] = []
            if len(possiblemods[num]) < 2:
                possiblemods[num].append(left+1)
                result.append(((left+1), num))
            curr = curr[1:]
            left += 1
        right += 1
    return [possiblemods, result]

def cum_sum(nums):
    curr = 0
    result = [0]*len(nums)
    for idx, num in enumerate(nums):
        curr += num
        result[idx] = curr
    return result

i = 1
while i < len(lines):
    s = lines[i]
    snums = list(map(int, s))
    CS = cum_sum(snums)
    # print(CS)
    w, m = map(int, lines[i+1].split(" "))
    i+=2
    queries = []
    while m > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        m-=1
        i+=1
    possiblemods, subsetsums = subsums(s, w)
    # print(possiblemods)
    # print(subsetsums)
    for l, r, k in queries:
        found = [-1, -1]
        currval = (CS[r-1] - (CS[l-2] if l-2 >= 0 else 0))% 9
        for idx, mod in subsetsums:
            if found != [-1, -1]: break
            currmod = (mod*currval) % 9
            lookingfor = -1
            if currmod == k:
                lookingfor = 0
            elif currmod >= k:
                lookingfor = 9 - currmod + k
            else:
                lookingfor = k - currmod
            if lookingfor in possiblemods:
                for pos in possiblemods[lookingfor]:
                    if pos != idx:
                        found = [idx, pos]
                        # print(possiblemods[lookingfor], found)
                        break
        print(*found)

