from math import gcd
import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for ii in range(1, len(lines), 2):
    xs = list(map(int, lines[ii+1].split()))
    gcdarr = [gcd(xs[i], xs[i+1]) for i in range(len(xs) - 1)]
    # print("Nums", xs)
    # print("gcdarr", gcdarr)
    #

    def test(candidate):
        if candidate < 0 or candidate >= len(xs):
            return False
        ys = [xs[i] for i in range(len(xs)) if i != candidate]
        gcdarr = [gcd(ys[i], ys[i+1]) for i in range(len(ys) - 1)]
        # print("candidate", candidate)
        # print("new gcdarr", gcdarr)
        result = True
        result = all(gcdarr[i] <= gcdarr[i+1] for i in range(len(gcdarr) - 1))
        # print("result", result)
        return result
    result = all(gcdarr[i] <= gcdarr[i+1] for i in range(len(gcdarr) - 1))
    for i in range(len(gcdarr) - 1):
        if gcdarr[i] > gcdarr[i+1]:
            for d in range(-2, 3):
                result |= test(i+d)
            break
    print("YES" if result else "NO")
