import sys
if sys.argv[-1] == "--debug":
    sys.stdin = open("in")
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using d::jjk

for line in lines[1:]:
    n = int(line)
    result = []
    for a in range(1, 10001):
        low = 1
        high = 10000
        while low < high:
            mid = (low + high) >> 1
            b = mid
            actual = n*a - b
            if actual < 0:
                high = mid
                continue
            digit_len = len(str(actual)) if actual else 0
            new_len = a - b
            if new_len > digit_len:
                low = mid + 1
            elif new_len < digit_len:
                high = mid
            elif new_len == digit_len:
                intvalue = 0 if a-b == 0 else int((a-b)*str(n))
                # print("intval", intvalue, b)
                if intvalue <= actual:
                    low = mid + 1
                else:
                    high = mid
            else:
                assert False
        # print(a, low)
        low -= 1
        actual = n*a - low
        digit_len = len(str(actual))
        if digit_len == a - low and low != 0:
            if int((a - low) * str(n)) == n*a - low:
                result.append((a, low))
    print(len(result))
    for a, b in result:
        print(a, b)
