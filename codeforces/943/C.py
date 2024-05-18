import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    xs = list(map(int, line.split()))
    curr = 10**8
    result = []
    for x in xs[::-1]:
        result.append(curr - x)
        curr = result[-1]
    result.reverse()
    result.append(result[-1] + xs[-1])
    assert [result[i] % result[i-1] for i in range(1, len(result))] == xs
    print(' '.join(map(str, result)))
