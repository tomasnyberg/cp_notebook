import sys

n, t= map(int, input().split(" "))
k = int(input())

print("?", 1, n)
sys.stdout.flush()
total = int(input())
target = total - k

low = 1
high = n
while low < high:
    mid = (low + high) >> 1
    print("?", low, high)
    sys.stdout.flush()
    # read an integer x from stdin
    x = int(input())
    if x >= target:
        low = mid + 1
    else:
        high = mid
print("!", low-1)