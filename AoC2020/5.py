import sys
lines = list(map(str.strip, sys.stdin.readlines()))

result = 0
seats = []
for line in lines:
    s = line
    first_7 = s[:7][::-1]
    row = 0
    for i in range(len(first_7)):
        if first_7[i] == 'B':
            row |= (1 << i)
    last_3 = s[7:][::-1]
    col = 0
    for i in range(len(last_3)):
        if last_3[i] == 'R':
            col |= (1 << i)
    id = row*8 + col
    seats.append(id)
    result = max(result, (row * 8 + col))
seats = set(seats)
print("Part one:", result)
for i in range(min(seats), max(seats)):
    if i not in seats:
        print("Part two:", i)
        break
