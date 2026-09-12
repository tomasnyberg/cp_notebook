import sys
if sys.argv[-1] == '--debug':
    sys.stdin = open('in')
lines = list(map(str.strip, sys.stdin.readlines()))
# TODO Remember to add int wrapping if using dict

for line in lines[2::2]:
    nums = list(map(int, line.split(" ")))
    ones = sum(nums)
    zeroes = len(nums) - ones
    print("Bessie" if ones>=zeroes else "Elsie")


