import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, k = map(int, lines[i].split(" "))
    s = lines[i+1]
    counts = {}
    for c in s:
        counts[c] = 1 if c not in counts else counts[c] + 1
    pairs = 0
    singles = 0
    for key in counts:
        pairs += counts[key] // 2
        singles += counts[key] % 2
    if k == 1:
        print(pairs*2 + (1 if singles != 0 else 0))
        continue
    pairs_for_everyone = pairs // k
    result = pairs_for_everyone * 2
    remaining = (pairs - (pairs_for_everyone)*k)*2 + singles
    # print("PFE", pairs_for_everyone)
    # print("pairs", pairs)
    # print("remaining", remaining)
    if remaining >= k:
        print(pairs_for_everyone * 2 + 1)
    else:
        print(pairs_for_everyone*2)