import sys

lines = list(map(str.strip, sys.stdin.readlines()))

def ones(n):
    return sum([1 for x in bin(n) if x == '1'])

factorials = [1]
for i in range(2, 15):
    factorials.append(i*factorials[-1])

pows_of_two = set()
for i in range(50):
    pows_of_two.add(1 << i)

sums_of_factorials = set([(1, 1)])
for factorial in factorials[1:]:
    temp_set = set()
    for total, count in sums_of_factorials:
        if factorial + total not in pows_of_two:
            temp_set.add((factorial + total, count + 1))
    sums_of_factorials = sums_of_factorials.union(temp_set)

for i in range(1, len(lines)):
    n = int(lines[i])
    smallest = ones(n)
    for total, count in sums_of_factorials:
        smallest = min(smallest, ones(n-total) + count)
    print(smallest)

print(factorials)
