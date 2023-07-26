import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    n , k = map(int, lines[ii].split())
    nums = list(map(int, lines[ii+1].split()))
    nums = list(enumerate(nums))
    def recur(bit, candidates):
        if bit < 0:
            return [0, 0, -1]
        zeroes = [(idx, x) for idx, x in candidates if x & (1 << bit) == 0]
        ones = [(idx, x) for idx, x in candidates if x & (1 << bit)]
        result = [0, 0, ((candidates[0][0], candidates[1][0]) if len(candidates) >= 2 else -1)]
        if len(zeroes) >= 2:
            tot, x, cs = recur(bit-1, zeroes)
            if cs == -1:
                cs = (zeroes[0][0], zeroes[1][0])
            tot += (1 << bit)
            x |= (1 << bit)
            result = max(result, [tot, x, cs])
        if len(ones) >= 2:
            tot, x, cs = recur(bit-1, ones)
            if cs == -1:
                cs = (ones[0][0], ones[1][0])
            tot += (1 << bit)
            result = max(result, [tot, x, cs])
        if len(zeroes) < 2 and len(ones) < 2:
            tot, x, cs = recur(bit-1, candidates)
            if cs == -1:
                cs = result[2]
            result = max(result, [tot, x, cs])
        return result
    _, x, (a,b) = (recur(k-1, nums))
    print(a+1, b+1, x)


