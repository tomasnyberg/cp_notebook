import sys, math
lines = list(map(str.strip, sys.stdin.readlines()))

def ones_complement(n):
    # Find number of bits in
    # the given integer
    number_of_bits = (int)(math.floor(math.log(n)/math.log(2))) + 1;
    # XOR the given integer with poe(2,
    # number_of_bits-1 and print the result
    return ((1 << number_of_bits) - 1) ^ n;

for line in lines[1:]:
    alreadymapped = set()
    n, k = map(int, line.split(" "))
    nums = [i for i in range(n)]
    maps = []
    def map_to_complement():
        for num in nums[1:][::-1]:
            if num in alreadymapped: continue
            comp = ones_complement(num)
            if comp in alreadymapped:
                comp = 0
            alreadymapped.add(comp)
            alreadymapped.add(num)
            maps.append((num, comp))
    if k == n-1:
        if n == 4:
            print(-1)
            continue
        maps.append((n-1, n-2))
        maps.append((n-3, 1))
        alreadymapped.update([n-1, n-2, n-3, 1])
    if k > 0 and k < n-1:
        maps.append((k, n-1))
        alreadymapped.update([k, n-1])
    map_to_complement()
    for a, b in maps:
        print(a, b)



