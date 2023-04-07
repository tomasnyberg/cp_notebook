import sys
# Read one number from stdin
n = int(input())
result = [-1]*n
for i in range(1, n-1, 3):
    print("?", i, i+2)
    sys.stdout.flush()
    allthree = int(input())
    print("?", i, i+1)
    sys.stdout.flush()
    firsttwo = int(input())
    print("?", i+1, i+2)
    sys.stdout.flush()
    lasttwo = int(input())
    result[i-1] = allthree - lasttwo
    result[i+1] = allthree - firsttwo
    result[i] = allthree - result[i-1] - result[i+1]
# We have one number at the end we have to get
if n % 3 == 1:
    print("?", n-1, n)
    sys.stdout.flush()
    lasttwo = int(input())
    result[-1] = lasttwo - result[-2]
# We have two numbers at the end to get and we can make 2 queries
if n % 3== 2:
    print("?", n-2, n-1)
    sys.stdout.flush()
    twobeforelast = int(input())
    result[-2] = twobeforelast - result[-3]
    print("?", n-1, n)
    sys.stdout.flush()
    lasttwo = int(input())
    result[-1] = lasttwo - result[-2]

print("!", *result)