import sys

n, t= map(int, input().split(" "))
k = int(input())

print("?", 1, n)
sys.stdout.flush()
total = int(input())
target = total - k

print("our target is", target)

low = 1
high = n
while low < high:
    mid = (low + high) >> 1
    print("?", 1, mid)
    sys.stdout.flush()
    x = int(input())
    if x >= target:
        low = mid + 1
    else:
        high = mid
print("!", low-1)