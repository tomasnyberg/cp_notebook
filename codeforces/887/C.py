import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict
# for ii in range(1, len(lines), 2):
#     n, k = map(int, lines[ii].split())
#     a = list(map(int, lines[ii + 1].split()))
#     max_a = max(a)
#     aset = set(a)
#     nums = [i+1 for i in range(100000)]
#     diffs = {}
#     for ck in range(k):
#         print("nums after", ck, "iterations", nums[:25])
#         curr = nums[0]
#         nums = [x for i, x in enumerate(nums) if i + 1 not in aset]
#         next = nums[0]
#     print()

# nums after 0 iterations [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# nums after 1 iterations [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 31, 32, 33, 34, 35]
# nums after 2 iterations [3, 5, 8, 9, 12, 14, 17, 18, 21, 23, 26, 27, 30, 31, 33, 34, 36, 37, 39, 40, 41, 42, 43, 44, 45]
# nums after 3 iterations [5, 8, 12, 14, 18, 21, 26, 27, 31, 33, 36, 37, 40, 41, 43, 44, 46, 47, 49, 50, 51, 52, 53, 54, 55]
# nums after 4 iterations [8, 12, 18, 21, 27, 31, 36, 37, 41, 43, 46, 47, 50, 51, 53, 54, 56, 57, 59, 60, 61, 62, 63, 64, 65]
# nums after 5 iterations [12, 18, 27, 31, 37, 41, 46, 47, 51, 53, 56, 57, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 74, 75]
# nums after 6 iterations [18, 27, 37, 41, 47, 51, 56, 57, 61, 63, 66, 67, 70, 71, 73, 74, 76, 77, 79, 80, 81, 82, 83, 84, 85]
# nums after 7 iterations [27, 37, 47, 51, 57, 61, 66, 67, 71, 73, 76, 77, 80, 81, 83, 84, 86, 87, 89, 90, 91, 92, 93, 94, 95]
# nums after 8 iterations [37, 47, 57, 61, 67, 71, 76, 77, 81, 83, 86, 87, 90, 91, 93, 94, 96, 97, 99, 100, 101, 102, 103, 104, 105]
# nums after 9 iterations [47, 57, 67, 71, 77, 81, 86, 87, 91, 93, 96, 97, 100, 101, 103, 104, 106, 107, 109, 110, 111, 112, 113, 114, 115]
# nums after 10 iterations [57, 67, 77, 81, 87, 91, 96, 97, 101, 103, 106, 107, 110, 111, 113, 114, 116, 117, 119, 120, 121, 122, 123, 124, 125]

for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii + 1].split()))
    if a[0] != 1:
        print(1)
        continue
    a.reverse()
    curr = 1
    increment_by = 0
    for _ in range(k):
        while a and curr >= a[-1]:
            increment_by += 1
            a.pop()
        curr += increment_by
    print(curr)



