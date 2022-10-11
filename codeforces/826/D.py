import sys
lines = list(map(str.strip, sys.stdin.readlines()))

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    result = [0]
    def merge_sort(xs, result):
        if len(xs) == 1: return xs
        left = xs[:len(xs)//2]
        right = xs[len(xs)//2:]
        leftmax = max(left)
        rightmax = max(right)
        # TODO: figure this out, i.e. when it is -1
        # if abs(leftmax - rightmax) > 1:
        #     result[0] = -10**9
        if leftmax > rightmax:
            if abs(min(left) - max(right)) > 1:
                result[0] = -10**9
            result[0] += 1
            return merge_sort(right, result) + merge_sort(left, result)
        else:
            if abs(max(left) - min(right)) > 1:
                result[0] = -10**9
            return merge_sort(left, result) + merge_sort(right, result)
    merge_sort(nums, result)
    print(result[0] if result[0] >= 0 else -1)
        
        
