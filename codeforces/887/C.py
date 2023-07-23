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
# nums after 1 iterations [2, 3, 5, 6, 8, 10, 11, 13, 14, 16, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
# nums after 2 iterations [3, 5, 8, 10, 13, 16, 19, 22, 23, 25, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
# nums after 3 iterations [5, 8, 13, 16, 22, 25, 28, 31, 32, 34, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
# nums after 4 iterations [8, 13, 22, 25, 31, 34, 37, 40, 41, 43, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]
# nums after 5 iterations [13, 22, 31, 34, 40, 43, 46, 49, 50, 52, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
# nums after 6 iterations [22, 31, 40, 43, 49, 52, 55, 58, 59, 61, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
# nums after 7 iterations [31, 40, 49, 52, 58, 61, 64, 67, 68, 70, 73, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
# nums after 8 iterations [40, 49, 58, 61, 67, 70, 73, 76, 77, 79, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
# nums after 9 iterations [49, 58, 67, 70, 76, 79, 82, 85, 86, 88, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
for ii in range(1, len(lines), 2):
    n, k = map(int, lines[ii].split())
    a = list(map(int, lines[ii + 1].split()))
    if a[0] != 1:
        print(1)
        continue
    a.reverse()
    curr = 1
    increment_by = 0
    for i in range(k):
        curr += increment_by
        while a and curr >= a[-1]:
            increment_by += 1
            curr += 1
            a.pop()
        # print("iteration", i+1, curr)
    print(curr)



