# Left shift all elements in array starting from start and ending at end by k steps
def left_rotate(arr, start, end, k):
    result = arr.copy()
    n = end-start+1
    k %= n 
    for i in range(start, end+1):
        result[(i-start-k)%n+start] = arr[i]
    return result

# Ex rotating array [1,2,3,4,5] between indexes 1 and 3 two steps, giving [1,4,2,3,5]
# left_rotate([1,2,3,4,5], 1, 3, 2)
print(left_rotate([1,2,3,4,5], 1, 3, 2))

def right_rotate(arr,start,end, k):
    result = arr.copy()
    n = end-start + 1
    k %= n
    for i in range(start, end+1):
        result[(i-start+k)%n+start] = arr[i]
    return result
# The below results in [1,3,4,2,5]
print(right_rotate([1,2,3,4,5], 1,3,2))
        
# Alternatively, just a method to do both since the only thing we are changing is the direction
# (I like having to separate ones since there's so many params and it's easy to mess up otherwise)
# Rotates right if dir is truthy
def rotate_arr(arr,start,end, k, dir):
    result = arr.copy()
    n = end-start + 1
    k %= n
    k = -k if not dir else k
    for i in range(start, end+1):
        result[(i-start+k)%n+start] = arr[i]
    return result

print(rotate_arr([1,2,3,4,5], 1,3,2, False))