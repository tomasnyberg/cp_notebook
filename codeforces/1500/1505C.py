import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines:
    mapped_to_ord = list(map(lambda x: ord(x) - ord('A'), line))
    bad = False
    for i in range(2, len(mapped_to_ord)):
        prevtwo = (mapped_to_ord[i-2] + mapped_to_ord[i-1]) % 26
        if prevtwo != mapped_to_ord[i]:
            bad = True
            break
    print("NO" if bad else "YES")
