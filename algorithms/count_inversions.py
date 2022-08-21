# Merge sort that counts inversions, expects an array of ints and an array with a single elem
# Example usage: 
# result = [0]
# merge_sort([4,1,4,6,7,7,5], result)
# This stores the amount of inversions in result[0], 6 for the above example
# Note that it includes equal elements in the inversions
def merge_sort(xs, result):
    def merge(left, right, result):
        a = 0
        b = 0
        merged = []
        while a < len(left) or b < len(right):
            if a == len(left) or b == len(right):
                merged += left[a:]
                merged += right[b:]
                break
            # Note, you can change this to < if you don't want to count an equal element as an inversion
            if left[a] <= right[b]:
                merged.append(left[a])  
                a += 1
            else:
                merged.append(right[b])
                b += 1
                result[0] += len(left) - a
        return merged
    if len(xs) == 1:
        return xs
    n = len(xs)
    return merge(merge_sort(xs[:n//2], result), merge_sort(xs[n//2:], result), result)

result = [0]
print(merge_sort([4,1,4,6,7,7,5], result), result)
