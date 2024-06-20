import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

ii = 1
while ii < len(lines):
    n, m = map(int, lines[ii].split())
    ii += 1
    a = []
    b = []
    for _ in range(n):
        a.append(list(map(int, lines[ii].split())))
        ii += 1
    for _ in range(n):
        b.append(list(map(int, lines[ii].split())))
        ii += 1

    def all_equal(a, b):
        return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a[0])))

    def transpose(m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

    def print_m(m):
        for row in m:
            print(row)

    def all_rows_same(a, b):
        rowset = {}
        for i in range(len(a)):
            rowset[min(a[i])] = set(a[i])
        for i in range(len(b)):
            if min(b[i]) not in rowset:
                return False
            expected = rowset[min(b[i])]
            actual = set(b[i])
            if expected != actual:
                return False
        return True

    def swap_around():
        rows = {}
        for i in range(len(b)):
            for j in range(len(b[0])):
                rows[b[i][j]] = i
        for i in range(len(a)):
            for j in range(len(a[0])):
                expected_row = rows[a[i][j]]
                while expected_row != i:
                    a[i], a[expected_row] = a[expected_row], a[i]
                    expected_row = rows[a[i][j]]
    if not all_rows_same(a, b):
        print("NO")
        continue
    a = transpose(a)
    b = transpose(b)
    if not all_rows_same(a, b):
        print("NO")
        continue
    # print("Before swapping first time")
    # print_m(a)
    # print()
    # print_m(b)
    swap_around()
    # print()
    # print("After swapping first time")
    # print_m(a)
    # print()
    # print_m(b)
    a = transpose(a)
    b = transpose(b)
    swap_around()
    # print()
    # print("After swapping second time")
    # print_m(a)
    # print()
    # print_m(b)
    print("YES" if all_equal(a, b) else "NO")
