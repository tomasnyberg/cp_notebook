import sys
lines = list(map(str.strip, sys.stdin.readlines()))

i = 1
while i < len(lines):
    n, q = map(int, lines[i].split(" "))
    i+=1
    nums = list(map(int, lines[i].split(" ")))
    queries = []
    i+=1
    while q > 0:
        queries.append(list(map(int, lines[i].split(" "))))
        q-=1
        i+=1
    evens = 0
    odds = 0
    total = sum(nums)
    for x in nums:
        if x % 2 == 1:
            odds +=1
        else:
            evens +=1
    for odd, amount in queries:
        if odd:
            total += amount * odds
            if amount % 2 == 1:
                evens += odds
                odds = 0
        else:
            total += amount * evens
            if amount % 2 == 1:
                odds += evens
                evens = 0
        print(total)