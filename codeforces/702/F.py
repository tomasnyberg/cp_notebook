import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    counts = {}
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
    biggestamount = 0
    for x, amount in counts.items():
        biggestamount = max(biggestamount, amount)
    result = 10**9
    # print(counts)
    for i in range(biggestamount+1):
        candidate = 0
        for x, amount in counts.items():
            if amount < i:
                candidate += amount
            else:
                candidate += amount - i
        # print(i, candidate)
        result = min(candidate, result)
    print(result)
    # print("\n\n")
