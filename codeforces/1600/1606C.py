import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for i in range(1, len(lines), 2):
    n, remaining = map(int, lines[i].split(" "))
    nums = list(map(int, lines[i+1].split(" ")))
    possible_values = []
    nums.sort()
    for num in nums:
        possible_values.append(10**num)
    result = 0
    remaining += 1
    for j in range(0, len(possible_values) - 1):
        if possible_values[j] * remaining < possible_values[j+1]:
            result += possible_values[j] * remaining
            remaining = 0
            break
        else:
            result += possible_values[j] * ((possible_values[j+1] // possible_values[j]) - 1)
            remaining -= ((possible_values[j+1] // possible_values[j]) - 1)
    if remaining > 0:
        result += remaining * possible_values[-1]
    print(result)