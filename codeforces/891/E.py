import sys
lines = list(map(str.strip, sys.stdin.readlines()))
import bisect
# TODO Remember to add int wrapping if using dict

def fast_absolute_difference_sum(arr):
    # Sort the array and compute the prefix sum for easy computation of sum of elements less than a[i]
    sorted_arr = sorted(arr)
    prefix_sum = [0]
    for num in sorted_arr:
        prefix_sum.append(prefix_sum[-1] + num)
    
    results = []
    for i in arr:
        # count_leq = len([x for x in sorted_arr if x <= i])
        count_leq = bisect.bisect_left(sorted_arr, i)
        sum_leq = prefix_sum[count_leq]
        sum_gt = prefix_sum[-1] - sum_leq
        result = i * count_leq - sum_leq + sum_gt - i * (len(arr) - count_leq) + len(arr)
        results.append(result)
    
    return results
for line in lines[2::2]:
    a = list(map(int, line.split()))
    # for i in range(len(a)):
    #     curr = 0
    #     for j in range(len(a)):
    #         curr += abs(a[i] - a[j]) + 1
    #     print(curr, end=' ')
    # print()
    print(*fast_absolute_difference_sum(a))
    
            
