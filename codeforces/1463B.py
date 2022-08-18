import sys, math, bisect
lines = list(map(str.strip, sys.stdin.readlines()))

def divisors(n):
    result = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result


for i in range(1, len(lines), 2):
    nums = list(map(int, lines[i+1].split(" ")))
    S = sum(nums)
    ans = [nums[0]]
    for j in range(1, len(nums)):
        divs1 = divisors(nums[j])
        divs2 = divisors(ans[j-1])
        if nums[j] > ans[j-1]:
            div = nums[j] // ans[j-1]
            divs2.append(div*ans[j-1])
            divs2.append((div+1)*ans[j-1])
        closest = (10**18, -1) # How close, what number
        for divs in [divs1, divs2]:
            for div in divs[::-1]:
                if ans[j-1] % div == 0 or div % ans[j-1] == 0:
                    if abs(nums[j] - ans[j-1]) < closest[0]:
                        closest = (abs(nums[j] - div), div)
        ans.append(closest[1])
    bad = 2*(sum([abs(ans[j] - nums[j]) for j in range(len(ans))]))
    # assert(bad <= S)
    # print(bad)
    [print(x,end=" ") for x in ans]
    print()