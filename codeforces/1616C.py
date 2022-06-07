# Might need to change this one slightly
def sum_of_sub(xs, left, right):
    res = 0
    for x in xs[left:right+1]:
        res += x
    return res

example = [3,4,6,8,11,2,7]
def good_subarray(xs, left, right):
    subsum = sum_of_sub(xs, left, right)
    expression = (xs[left] + xs[right])*(right - left + 1)/2
    return subsum == expression
s = set()

for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            for l in range(1, 11):
                for ö in range(1, 11):
                    for ä in range(1, 11):
                        if good_subarray([i,j,k, l, ö, ä], 0, 5):
                            s.add((i+j+k+l+ö+ä))
print(s)
print(len(s))