import sys
if sys.argv[-1] == "--debug":
    sys.stdin = open("in")
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using d::jjk


def gen_str(n, a, b):
    n_str = str(n)
    n_str_len = len(str(n))
    remaining_chars = n_str_len*a - b
    circular = n_str_len - 1 - (b % n_str_len)
    str_candidate = []
    for _ in range(remaining_chars):
        str_candidate.append(n_str[circular])
        circular -= 1
        circular %= n_str_len
    str_candidate = "".join(str_candidate[::-1])
    return str_candidate


for line in lines[1:]:
    n = int(line)
    n_str = str(n)
    n_str_len = len(str(n))
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
            new_len = a*n_str_len - b
            if new_len > digit_len:
                low = mid + 1
            elif new_len < digit_len:
                high = mid
            elif new_len == digit_len:
                if new_len == 0:
                    high = mid
                    continue
                # print(a*str(n)[:-b], a, b, n)
                str_actual = str(actual)
                # remaining_chars = n_str_len*a - b
                # circular = n_str_len - 1 - (b % n_str_len)
                # str_candidate = []
                # for _ in range(remaining_chars):
                #     str_candidate.append(n_str[circular])
                #     circular -= 1
                #     circular %= n_str_len
                # # print("intval", intvalue, b)
                str_candidate = gen_str(n, a, b)
                if str_candidate <= str_actual:
                    low = mid + 1
                else:
                    high = mid
            else:
                assert False
        # print(a, low)
        low -= 1
        actual = n*a - low
        digit_len = len(str(actual))
        if digit_len == a*len(n_str) - low and low != 0:
            if gen_str(n, a, low) == str(actual):
                result.append((a, low))
    print(len(result))
    for a, b in result:
        print(a, b)
