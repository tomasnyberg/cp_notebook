import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[1:]:
    both, alice, bob, neither = map(int, line.split())
    if both == 0:
        print(1 if alice + bob + neither > 0 else 0)
        continue
    result = both
    result += min(alice, bob)*2
    small = min(alice, bob)
    alice -= small
    bob -= small
    remaining = alice + bob + neither
    result += min(both + 1, remaining)
    # print()
    # print(both, alice, bob, neither)
    print(result)
    # print()
    