import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n , k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    def recur(bit, candidates):
        if bit < 0:
            return 0
        zeroes = [x for x in candidates if x & (1 << bit) == 0]
        ones = [x for x in candidates if x & (1 << bit)]
        result = 0
        if len(zeroes) >= 2:
            result = max(result, (1 << bit) + recur(bit-1, zeroes))
        elif len(ones) >= 2:
            result = max(result, (1 << bit) + recur(bit-1, ones))
        else:
            result = recur(bit-1, candidates)
        return result
    print(recur(k-1, nums))


