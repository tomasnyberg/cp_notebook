# slides a window of size size along xs, in this case it counts the sum, but could be modified

def sliding_window(xs, size):
    count = 0
    left = 0
    right = 0
    while right < len(xs):
        count += (xs[right])
        if right - left >= size - 1:
            print(xs[left:right+1], count)
            count -= xs[left]
            left += 1
        right += 1

xs = [1,2,3,4,5,6,7,8]
# Example, slide a window of size 5 over the array above, giving the following
# [1, 2, 3, 4, 5] 15
# [2, 3, 4, 5, 6] 20
# [3, 4, 5, 6, 7] 25
# [4, 5, 6, 7, 8] 30
print(sliding_window(xs, 5))