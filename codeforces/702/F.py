import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    counts = {}
    for x in nums:
        counts[x] = 1 if x not in counts else counts[x] + 1
    amounts = set()
    for x, amount in counts.items():
        amounts.add(amount)
    result = 10**9
    # print(counts)
    looks = 0
    for i in amounts:
        candidate = 0
        for x, amount in counts.items():
            looks += 1
            if amount < i:
                candidate += amount
            else:
                candidate += amount - i
        # print(i, candidate)
        result = min(candidate, result)
    # print(len(nums), looks)
    print(result)
    # print("\n\n")
