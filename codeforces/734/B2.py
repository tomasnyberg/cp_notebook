import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines),2 ):
    n, k= map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    numscopy = nums.copy()
    amount_colored = {}
    nums.sort()
    currcolor = 1
    for x in nums:
        if x not in amount_colored: amount_colored[x] = set()
        if len(amount_colored[x]) == k: continue
        amount_colored[x].add(currcolor)
        currcolor += 1
        if currcolor == k+1:
            currcolor = 1
    colored = {}
    result = []
    for x in numscopy:
        if x not in amount_colored:
            result.append(0)
            continue
        curr = amount_colored[x].pop()
        colored[curr] = 1 if curr not in colored else colored[curr] + 1
        result.append(curr)
        if not amount_colored[x]: del amount_colored[x]
    # print(result)
    smallest = min([colored[key] for key in colored])
    for idx, x in enumerate(result):
        if x and colored[x] > smallest:
            result[idx] = 0
            colored[x] -= 1
    # print(result)
    assert(len(result) == len(nums))
    [print(x, end=" ") for x in result]
    print()

