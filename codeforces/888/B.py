import sys
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split()))
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 == 1]
    evens.sort(reverse=True)
    odds.sort(reverse=True)
    xs = []
    for x in nums:
        if x % 2 == 0:
            xs.append(evens.pop())
        else:
            xs.append(odds.pop())
    print("YES" if xs == list(sorted(nums)) else "NO")
